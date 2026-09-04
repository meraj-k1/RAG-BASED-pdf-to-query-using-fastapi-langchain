import os
import tempfile
import uuid

from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .ingestion import ingest_pdf
from .rag_chain import ask as ask_rag

app = FastAPI(title="RAG-Based PDF Question Answering API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/ingest")
async def ingest(file: UploadFile = File(...), collection:str | None = Form(None)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    save_path = os.path.join(tempfile.gettempdir(), f"{uuid.uuid4().hex}.pdf")

    with open(save_path, "wb") as f:
        f.write(await file.read())

    try:
        return ingest_pdf(save_path, collection)
    finally:
        try:
            os.remove(save_path)
        except OsError:
            pass

class AskRequest(BaseModel):
    question: str
    collection: str | None = None
    k: int | None = None

@app.post("/ask")
def ask(request: AskRequest):
    try:
        return ask_rag(
        collection=request.collection or "pdf_docs",
        question=request.question,
        k=request.k or 4
    )
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

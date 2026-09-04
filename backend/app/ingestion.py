"""PDF ingestion module: load -> split -> embed -> store in vector database."""
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from .db import add_documents_to_collection

def ingest_pdf(file_path: str, collection: str | None = None):
    """Ingest a PDF file into the vector database."""
    if collection is None:
        collection = "pdf_docs"

    loader = PyPDFLoader(file_path)
    docs = loader.load() 

    chunks = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    ).split_documents(docs)

    add_documents_to_collection(collection, chunks) # embed + write FAISS collection

    return {
        "pages": len(docs),
        "chunks": len(chunks),
        "collection": collection,
    }
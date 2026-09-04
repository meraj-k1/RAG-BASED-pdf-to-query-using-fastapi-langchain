# 📄 RAG PDF QA

A **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask natural-language questions. Answers are generated using information retrieved directly from the uploaded PDF.

## 🚀 Features

* 📤 Upload PDF documents
* 🔍 Semantic document search
* 🤖 AI-powered question answering
* 📚 FAISS vector database
* ⚡ FastAPI backend
* 🎨 Streamlit frontend
* 🧠 Local sentence-transformers embeddings
* 🔐 Groq LLM integration
* 🐳 Docker support

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Frontend:** Streamlit
* **LLM:** Groq — Llama 3.3 70B
* **Embeddings:** all-MiniLM-L6-v2
* **Vector Store:** FAISS
* **Framework:** LangChain
* **Deployment:** Docker / Render

## 📁 Project Structure

```text
RAG-Based/
├── backend/
│   ├── app/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd RAG-Based
```

### 2. Configure environment variables

```bash
cp .env.example .env
```

Add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Run with Docker

```bash
docker compose up --build
```

### 4. Run locally

**Backend:**

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

**Frontend:**

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

Frontend:

```text
http://localhost:8501
```

Backend API:

```text
http://localhost:8000
```

## 🔗 API Endpoints

| Method | Endpoint  | Description             |
| ------ | --------- | ----------------------- |
| GET    | `/health` | Health check            |
| POST   | `/ingest` | Upload and process PDF  |
| POST   | `/ask`    | Ask questions about PDF |

## 📌 How It Works

```text
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embeddings
 ↓
FAISS
 ↓
Similarity Search
 ↓
Relevant Context
 ↓
Groq LLM
 ↓
Answer
```

## 🔐 Environment Variables

Create `.env` from `.env.example`.

```env
GROQ_API_KEY=your_api_key
```

**Never commit your `.env` file or API keys to GitHub.**

## 📄 License

MIT License

```

এটা তোমার GitHub repository-এর জন্য **short + professional + recruiter-friendly** হবে। চাইলে আমি এটাকে আরও **premium GitHub README** বানিয়ে দিতে পারি, যেখানে badges, architecture diagram, screenshots এবং live demo section থাকবে।
```

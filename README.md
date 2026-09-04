# 📄 RAG PDF QA

A **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask natural-language questions based on the document content.

## 🚀 Features

* 📤 PDF upload
* 🔍 Semantic search
* 🤖 AI-powered Q&A
* 📚 FAISS vector store
* ⚡ FastAPI backend
* 🎨 Streamlit frontend
* 🧠 Local embeddings
* 🔐 Groq LLM
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

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd RAG-Based
```

### 2. Configure Environment

```bash
cp .env.example .env
```

Add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> Never commit your `.env` file or API keys to GitHub.

### 3. Run with Docker

```bash
docker compose up --build
```

### 4. Run Locally

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

Open:

```text
Frontend: http://localhost:8501
Backend:  http://localhost:8000
```

## 🔗 API Endpoints

| Method | Endpoint  | Description                 |
| ------ | --------- | --------------------------- |
| GET    | `/health` | Health check                |
| POST   | `/ingest` | Upload and process PDF      |
| POST   | `/ask`    | Ask questions about the PDF |

## 🔄 How It Works

```text
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embeddings
 ↓
FAISS Vector Store
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

Create a `.env` file from `.env.example`:

```env
GROQ_API_KEY=your_groq_api_key_here
```

## 📄 License

MIT License

# Intelligent-Document-Retrieval-System-using-RAG

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FAISS](https://img.shields.io/badge/VectorDB-FAISS-green)
![OpenAI](https://img.shields.io/badge/LLM-OpenAI-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 🧠 Overview

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline that enhances Large Language Models by injecting **relevant external knowledge** at runtime.

Unlike traditional LLM responses, this system:

* 🔍 Retrieves context from documents
* 🧩 Augments prompts with relevant data
* 🤖 Generates accurate, context-aware answers

---

## 🎥 Demo (ChatGPT-like Interaction)

![Chat Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2ZzZ2ZkY2RjY2V2a3V1M3ZkZm9zN3p1c3RkY2F1d2ZkM2F5eGd3ZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o7aD2saalBwwftBIY/giphy.gif)

---

## 🔄 RAG Pipeline Flow

![RAG Flow](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2h0d2F4b2x5a3F4a2p0N2k1aWJkZ3Z5YzR0cWl4d2V3Z2JzY2RrdiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l0MYt5jPR6QX5pnqM/giphy.gif)

---

## ⚙️ Architecture

```mermaid
flowchart LR
    A[User Query] --> B[Embedding]
    B --> C[FAISS Vector Search]
    C --> D[Retrieve Relevant Chunks]
    D --> E[Augmented Prompt]
    E --> F[LLM Response]
```

---

## 🛠️ Tech Stack

* **Python**
* **FAISS** – Vector similarity search
* **OpenAI API** – Embeddings + LLM
* **NumPy** – Vector operations
* **dotenv** – Environment variables

---

## 📁 Project Structure

```
mini-rag/
│── data/
│    └── sample.txt
│── rag.py
│── requirements.txt
│── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/rishi02soni/mini-rag.git
cd mini-rag
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

### 4️⃣ Run the Project

```bash
python rag.py
```

---

## 💡 Example Usage

```
Ask a question: What is AI?

Answer:
Artificial Intelligence (AI) is the simulation of human intelligence in machines.
```

---

## 🔍 Key Features

* ✅ Document chunking for efficient retrieval
* ✅ Embedding generation using OpenAI
* ✅ Fast similarity search with FAISS
* ✅ Context-aware response generation
* ✅ Lightweight & beginner-friendly

---

## ⚡ How It Works

1. 📄 Load document data
2. ✂️ Split into chunks
3. 🧠 Convert chunks into embeddings
4. 📦 Store in FAISS vector database
5. ❓ User query → embedding
6. 🔍 Retrieve most relevant chunks
7. 🤖 Send context to LLM → generate answer

---

## 🧪 API Interaction (Behind the Scenes)

![API Flow](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3d6b3o1d2F4eTh6YjF0a2J3d2FvM2J6bWQ5Z2xqY2R2dWZ0eXZsNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/26AHONQ79FdWZhAI0/giphy.gif)

* Embeddings API → converts text into vectors
* FAISS → retrieves similar vectors
* Chat API → generates final answer

---

## 🔥 Future Enhancements

* 📄 PDF / DOCX ingestion
* 🌐 Web-based UI (Streamlit / React)
* 🧠 Memory-based conversations
* 📊 Hybrid search (BM25 + Vector)
* ☁️ Deploy on AWS / Docker

---

## 💼 Resume Impact

**Project Title:**
*Context-Aware Question Answering System using RAG*

**Highlights:**

* Built an end-to-end RAG pipeline integrating vector search and LLMs
* Improved response accuracy using semantic retrieval
* Designed scalable embedding-based search architecture

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Show Your Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 🧠 Share with others

---

## 👨‍💻 Author

**Rishi Soni**

* Aspiring SDE | DevOps | AI Enthusiast 🚀

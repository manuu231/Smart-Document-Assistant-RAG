<div align="center">

# 🧠 Smart Document Assistant — RAG Pipeline

### An intelligent document assistant built with RAG
*Upload any text, ask any question, get accurate answers powered by Google Gemini and FAISS*

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.2+-green?style=for-the-badge&logo=chainlink&logoColor=white)
![Gemini](https://img.shields.io/badge/Google_Gemini-API-orange?style=for-the-badge&logo=google&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-Vector_DB-red?style=for-the-badge&logo=meta&logoColor=white)
![Colab](https://img.shields.io/badge/Google_Colab-Notebook-yellow?style=for-the-badge&logo=googlecolab&logoColor=white)

<br/>

> 🔍 **RAG = Retrieval Augmented Generation**
> Find relevant information from YOUR documents → Add to prompt → Generate accurate answers

<br/>

**Built by [Manpreet Kaur](https://github.com/manuu231)**
MS Data Science @ Clarkson University | AI/ML Engineer | 3+ Years @ Wipro

</div>

---

## 📌 What Does This Project Do?

Without RAG, AI models like Gemini cannot answer questions about **your private documents.**

This project solves that:

```
❌ Without RAG:   "Where does Manpreet work?" → "I don't know"
✅ With RAG:      "Where does Manpreet work?" → "Manpreet worked at Wipro as an ML Engineer"
```

You can point it at **any text document** and ask questions in plain English — it finds the right answer every time.

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 Python | 3.10+ | Programming language |
| 🔗 LangChain | 0.2+ | AI pipeline framework |
| 🤖 Google Gemini | gemini-2.5-flash | Generating final answers |
| 🔢 Gemini Embeddings | embedding-001 | Converting text → vectors |
| 🗄️ FAISS | CPU | Vector database — store and search embeddings |
| ✂️ RecursiveCharacterTextSplitter | — | Splitting documents into chunks |
| 📦 RetrievalQA | — | Connecting retriever + LLM |

---

## 🔄 How the Pipeline Works

```
📄  Your Text Document
         │
         ▼
✂️  Split into Chunks
    (chunk_size=200, overlap=50)
         │
         ▼
🔢  Convert to Vectors
    (GoogleGenerativeAIEmbeddings)
         │
         ▼
🗄️  Store in FAISS
    (Vector Database)
         │
         ▼
❓  You Ask a Question
         │
         ▼
🔍  Retriever Finds
    Top 2 Relevant Chunks
         │
         ▼
🤖  Gemini Reads Chunks
    + Generates Answer
         │
         ▼
✅  Accurate Answer
    with Source Chunks
```

---

## ⚙️ Setup and Installation

### Step 1 — Clone the Repository
```bash
git clone https://github.com/manuu231/smart-document-assistant-rag.git
cd smart-document-assistant-rag
```

### Step 2 — Open in Google Colab
Upload `day6_rag_pipeline.ipynb` to [Google Colab](https://colab.research.google.com)

### Step 3 — Install Dependencies
Run Cell 1 in the notebook:
```python
!pip install langchain langchain-google-genai langchain-community faiss-cpu langchain-core -q
```

### Step 4 — Set Up API Key Safely
> ⚠️ **Never hardcode your API key — always use Colab Secrets!**

1. Click 🔑 **Secrets** icon on left side of Colab
2. Click **Add new secret**
3. Name → `GEMINI_API_KEY`
4. Paste your Gemini API key
5. Toggle **Notebook access ON**

The notebook loads it safely:
```python
import os
from google.colab import userdata
os.environ["GOOGLE_API_KEY"] = userdata.get("GEMINI_API_KEY")
```

---

## 🚀 How to Use

Run all cells top to bottom, then use the `ask()` function:

```python
# Ask anything about your document!
ask("Where does Manpreet study?")
ask("What are her skills?")
ask("How many years of experience does she have?")
ask("What project did she complete?")
```

### Example Output
```
❓ QUESTION: Where does Manpreet study?
──────────────────────────────────────────────────
🤖 ANSWER:
Manpreet Kaur is an MS Data Science student at Clarkson University.

📚 SOURCE CHUNKS USED:
Chunk 1: Manpreet Kaur is an MS Data Science student at Clarkson University.
She has 3 years of experience as ML Engineer at Wipro...
```

---

## 📊 Pipeline Parameters

| Parameter | Value | Why This Value |
|-----------|-------|----------------|
| `chunk_size` | 200 | Small document — small chunks work best |
| `chunk_overlap` | 50 | Preserves meaning between chunk boundaries |
| `k` | 2 | Returns 2 most relevant chunks per question |
| `temperature` | 0.0 | Consistent factual answers — no creativity needed |
| `model` | gemini-2.5-flash | Fast, accurate, free with Gemini API |
| `embeddings` | embedding-001 | Google's best embedding model |

---

## 🔑 Key Concepts

<details>
<summary><b>What are Embeddings?</b></summary>
Converting text into numbers (vectors) so computers can understand meaning.
Similar meaning = similar numbers = FAISS finds them together!

```
"Manpreet works at Wipro"  →  [0.2, 0.8, 0.1, 0.9, ...]
"She is an ML Engineer"    →  [0.3, 0.7, 0.2, 0.8, ...]  ← similar!
"The sky is blue"          →  [0.9, 0.1, 0.8, 0.2, ...]  ← very different
```
</details>

<details>
<summary><b>What is FAISS?</b></summary>
Facebook AI Similarity Search — a free, open source vector database.
Stores your document vectors and finds the most similar ones when you ask a question.
Think of it as Google Search but for YOUR documents!
</details>

<details>
<summary><b>What is chunk_overlap?</b></summary>
When splitting a document, some characters are shared between consecutive chunks.
This prevents meaning from being cut off at chunk boundaries.

```
Without overlap:  "Manpreet works at Wipro as ML" | "Engineer with 3 years"
With overlap:     "Manpreet works at Wipro as ML" | "as ML Engineer with 3 years" ✅
```
</details>

---

## 📁 Project Structure

```
smart-document-assistant-rag/
│
├── day6_rag_pipeline.ipynb    ← Main RAG pipeline notebook
└── README.md                  ← This file
```

---

## 🔭 Coming Next 

| Day | Project | Status |
|-----|---------|--------|
| Day  1| LangChain Basics — Prompt Templates + LCEL | ✅ Done |
| Day 2 | Interview Bot — LangChain + Memory | ✅ Done |
| Day 3 | Smart Document Assistant — RAG Pipeline | ✅ Done |
| Day 4 | RAG with Real PDF Documents | 🔒 Coming |
| Day 5 | RAG with Multiple Documents | 🔒 Coming |
| Day 6 | Conversational RAG with Memory | 🔒 Coming |
| Day 7 | RAG Evaluation and Optimization | 🔒 Coming |

---

## 📄 License

MIT License — feel free to use, modify and share!

---

<div align="center">

⭐ **Star this repo if you found it helpful!**

Made with ❤️ by [Manpreet Kaur](https://github.com/manuu231)  

</div>

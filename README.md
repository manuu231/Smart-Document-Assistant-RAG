<div align="center">

# 🧠 Smart Document Assistant — RAG Pipeline

### An intelligent document assistant built with RAG
*Upload any text, ask any question, get accurate answers powered by Google Gemini and FAISS*

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.2+-green?style=for-the-badge&logo=chainlink&logoColor=white)
![Gemini](https://img.shields.io/badge/Google_Gemini-API-orange?style=for-the-badge&logo=google&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-Vector_DB-red?style=for-the-badge&logo=meta&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-Live_Demo-yellow?style=for-the-badge&logo=gradio&logoColor=white)
![Colab](https://img.shields.io/badge/Google_Colab-Notebook-orange?style=for-the-badge&logo=googlecolab&logoColor=white)

<br/>

### 🚀 [Live Demo on Hugging Face](https://huggingface.co/spaces/Manpreet02/smart-document-assistant-rag) | 📓 [Open in Colab](https://colab.research.google.com)

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

Paste **any text** — resume, article, notes, bio — ask any question — get accurate answers instantly!

---

## 🎯 Live Demo — Try it Now!

👉 **[Smart Document Assistant — Hugging Face Space](https://huggingface.co/spaces/Manpreet02/smart-document-assistant-rag)**

### How to use the live demo:
1. 📄 Paste any text in the Document box
2. ❓ Type your question about that text
3. 🚀 Click Ask
4. ✅ Get accurate answer with source chunks shown!

> No setup needed — just open the link and use it directly in your browser!

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 Python | Programming language |
| 🔗 LangChain | AI pipeline framework |
| 🤖 Google Gemini | Generating final answers |
| 🔢 Gemini Embeddings | Converting text to vectors |
| 🗄️ FAISS | Vector database — store and search embeddings |
| ✂️ RecursiveCharacterTextSplitter | Splitting documents into chunks |
| 📦 RetrievalQA | Connecting retriever + LLM |
| 🎨 Gradio | Web interface for live demo |
| 🤗 Hugging Face Spaces | Hosting the live demo |

---

## 🔄 How the Pipeline Works

```
📄  Your Text Document
         │
         ▼
✂️  Split into Chunks
    (chunk_size=500, overlap=100)
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
✅  Accurate Answer + Source Chunks
```

---

## 📁 Project Structure

```
smart-document-assistant-rag/
│
├── app.py                      ← Gradio web app (Hugging Face)
├── RAG_pipeline.ipynb     ← Google Colab notebook
├── requirements.txt            ← Dependencies
└── README.md                   ← This file
```

---

## ⚙️ Run Locally

### Step 1 — Clone
```bash
git clone https://github.com/manuu231/smart-document-assistant-rag.git
cd smart-document-assistant-rag
```

### Step 2 — Install
```bash
pip install -r requirements.txt
```

### Step 3 — Set API Key
```bash
export GOOGLE_API_KEY="your_gemini_key_here"
```

### Step 4 — Run Gradio App
```bash
python app.py
```

### Step 5 — Run Colab Notebook
- Open `RAG_pipeline.ipynb` in Google Colab
- Add `GEMINI_API_KEY` to Colab Secrets
- Run all cells top to bottom

---

## 🔐 API Key Safety

> ⚠️ **Never hardcode your API key anywhere!**

| Platform | How to store key safely |
|----------|------------------------|
| Hugging Face | Space Settings → Repository Secrets → `GOOGLE_API_KEY` |
| Google Colab | Secrets icon → Add `GEMINI_API_KEY` → Toggle ON |
| Local machine | Environment variable → `export GOOGLE_API_KEY="..."` |
| GitHub | Never commit key → add `.env` to `.gitignore` |

---

## 📊 Pipeline Parameters

| Parameter | Value | Why |
|-----------|-------|-----|
| `chunk_size` | 500 | Good balance for most documents |
| `chunk_overlap` | 100 | Preserves meaning at chunk boundaries |
| `k` | 2 | Returns 2 most relevant chunks |
| `temperature` | 0.0 | Consistent factual answers |
| `model` | gemini-1.5-flash | Fast and accurate |
| `embeddings` | models/gemini-embedding-001 | Google's best embedding model |

---

## 🔑 Key Concepts

<details>
<summary><b>What is RAG?</b></summary>

RAG = Retrieval Augmented Generation

- **Retrieval** → Find relevant information from your documents
- **Augmented** → Add that information to the prompt
- **Generation** → Let AI generate answer using that information

Without RAG → AI cannot answer about YOUR documents
With RAG → AI reads YOUR documents and answers accurately ✅
</details>

<details>
<summary><b>What are Embeddings?</b></summary>

Converting text into numbers (vectors) so computers can understand meaning.

```
"Manpreet works at Wipro"  →  [0.2, 0.8, 0.1, 0.9, ...]
"She is an ML Engineer"    →  [0.3, 0.7, 0.2, 0.8, ...]  ← similar meaning!
"The sky is blue"          →  [0.9, 0.1, 0.8, 0.2, ...]  ← very different!
```

Similar meaning = similar numbers = FAISS finds them together!
</details>

<details>
<summary><b>What is FAISS?</b></summary>

Facebook AI Similarity Search — a free open source vector database.
Stores your document vectors and finds the most similar ones instantly.
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

## 🔭 90 Day AI Engineering Journey

 Project | Links |
---------|-------|
LangChain Basics — Prompt Templates + LCEL | ✅ Done |
 Interview Bot — LangChain + Memory | ✅ Done |
 Smart Document Assistant — RAG Pipeline | ✅ [Live Demo](https://huggingface.co/spaces/Manpreet02/smart-document-assistant-rag) |
 RAG with Real PDF Documents | ✅ Done |
 RAG with Multiple Documents | 🔒 Coming |
 Conversational RAG with Memory | 🔒 Coming |
 RAG Evaluation and Optimization | 🔒 Coming |

---

## 📄 License

MIT License — feel free to use, modify and share!

---

<div align="center">

⭐ **Star this repo if you found it helpful!**

Made with ❤️ by [Manpreet Kaur](https://github.com/manuu231) 

🔗 [GitHub](https://github.com/manuu231) | 
🤗 [Hugging Face](https://huggingface.co/Manpreet02) | 
🚀 [Live Demo](https://huggingface.co/spaces/Manpreet02/smart-document-assistant-rag)

</div>

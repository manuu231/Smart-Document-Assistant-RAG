---
title: Smart Document Assistant RAG
emoji: 🧠
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 6.16.0
app_file: app.py
pinned: true
---

<div align="center">

# 🧠 Smart Document Assistant — RAG Pipeline

### An intelligent document assistant built with RAG
*Upload any text, ask any question, get accurate answers powered by Google Gemini and FAISS*

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.2+-green?style=for-the-badge&logo=chainlink&logoColor=white)
![Gemini](https://img.shields.io/badge/Google_Gemini-API-orange?style=for-the-badge&logo=google&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-Vector_DB-red?style=for-the-badge&logo=meta&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-Live_Demo-yellow?style=for-the-badge&logo=gradio&logoColor=white)

<br/>

🚀 **[Live Demo on Hugging Face](https://huggingface.co/spaces/Manpreet02/smart-document-assistant-rag)**

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

## 🎯 Live Demo

👉 **Try it here: [Smart Document Assistant](https://huggingface.co/spaces/Manpreet02/smart-document-assistant-rag)**

### How to use:
1. 📄 Paste any text in the Document box
2. ❓ Type your question about that text
3. 🚀 Click Ask
4. ✅ Get accurate answer with source chunks!

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 Python | Programming language |
| 🔗 LangChain | AI pipeline framework |
| 🤖 Google Gemini | Generating final answers |
| 🔢 Gemini Embeddings | Converting text to vectors |
| 🗄️ FAISS | Vector database |
| ✂️ RecursiveCharacterTextSplitter | Splitting documents into chunks |
| 🎨 Gradio | Web interface for live demo |

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

### Step 4 — Run
```bash
python app.py
```

---

## 🔐 API Key Safety

> ⚠️ **Never hardcode your API key!**

- **Hugging Face** → Add `GOOGLE_API_KEY` in Space Settings → Repository Secrets
- **Google Colab** → Add in Colab Secrets → use `userdata.get()`
- **Local** → Use environment variables → never commit to GitHub

---

## 📁 Project Structure

```
smart-document-assistant-rag/
│
├── app.py               ← Gradio web app
├── requirements.txt     ← Dependencies
└── README.md            ← This file
```

---

## 🔭 AI Engineering Journey

 Project | Status |
---------|--------|
 LangChain Basics — Prompt Templates + LCEL | ✅ Done |
 Interview Bot — LangChain + Memory | ✅ Done |
 Smart Document Assistant — RAG Pipeline | ✅ Done |
 RAG with Real PDF Documents |  ✅ Done |
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

🔗 [GitHub](https://github.com/manuu231) | 🤗 [Hugging Face](https://huggingface.co/Manpreet02)

</div>
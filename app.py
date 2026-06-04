import os
import gradio as gr

from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings
)

from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

# Load API key from Hugging Face Secrets
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

def build_rag_and_answer(document_text, question):
    """
    Takes a document and a question.
    Builds RAG pipeline and returns the answer.
    """

    # --- Validation ---
    if not document_text or document_text.strip() == "":
        return "⚠️ Please paste some text in the Document box first!", ""

    if not question or question.strip() == "":
        return "⚠️ Please type a question!", ""

    if not GOOGLE_API_KEY:
        return "⚠️ API key not found. Please add GOOGLE_API_KEY in Space Secrets!", ""

    try:
        # --- Step 1: Split document into chunks ---
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )
        chunks = splitter.split_text(document_text)

        # --- Step 2: Create embeddings ---
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=GOOGLE_API_KEY
        )

        # --- Step 3: Store in FAISS ---
        vectorstore = FAISS.from_texts(chunks, embeddings)

        # --- Step 4: Create retriever ---
        retriever = vectorstore.as_retriever(
            search_kwargs={"k": 2}
        )

        # --- Step 5: Create LLM ---
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0.0,
            google_api_key=GOOGLE_API_KEY
        )

        # --- Step 6: Create RAG chain ---
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            return_source_documents=True
        )

        # --- Step 7: Get answer ---
        result = qa_chain.invoke({"query": question})
        answer = result["result"]

        # --- Step 8: Get source chunks used ---
        sources = ""
        for i, doc in enumerate(result["source_documents"]):
            sources += f"📦 Chunk {i+1}:\n{doc.page_content}\n\n"

        return answer, sources

    except Exception as e:
        return f"❌ Error: {str(e)}", ""


# --- Gradio UI ---
with gr.Blocks(
    theme=gr.themes.Soft(),
    title="Smart Document Assistant"
) as app:

    # Header
    gr.Markdown("""
    # 🧠 Smart Document Assistant
    ### Powered by RAG + Google Gemini + FAISS
    
    **How to use:**
    1. 📄 Paste any text in the Document box (resume, article, notes, anything!)
    2. ❓ Type your question
    3. 🚀 Click Ask and get your answer!
    
    ---
    """)

    with gr.Row():
        # Left column — inputs
        with gr.Column(scale=1):
            document_input = gr.Textbox(
                label="📄 Your Document",
                placeholder="Paste any text here — resume, article, notes, bio...",
                lines=15,
                max_lines=30
            )

            question_input = gr.Textbox(
                label="❓ Your Question",
                placeholder="Ask anything about your document...",
                lines=2
            )

            ask_button = gr.Button(
                "🚀 Ask",
                variant="primary",
                size="lg"
            )

            # Example questions
            gr.Examples(
                examples=[
                    ["Manpreet Kaur is an MS Data Science student at Clarkson University. She has 3 years of experience as ML Engineer at Wipro. She is on STEM OPT till 2028. Her skills include Python, Machine Learning, LangChain, FAISS. She completed an Interview Bot project using LangChain and Gemini.", "Where does Manpreet study?"],
                    ["Manpreet Kaur is an MS Data Science student at Clarkson University. She has 3 years of experience as ML Engineer at Wipro. She is on STEM OPT till 2028. Her skills include Python, Machine Learning, LangChain, FAISS. She completed an Interview Bot project using LangChain and Gemini.", "What are her skills?"],
                    ["Manpreet Kaur is an MS Data Science student at Clarkson University. She has 3 years of experience as ML Engineer at Wipro. She is on STEM OPT till 2028. Her skills include Python, Machine Learning, LangChain, FAISS. She completed an Interview Bot project using LangChain and Gemini.", "What project did she complete?"],
                ],
                inputs=[document_input, question_input],
                label="💡 Try these examples!"
            )

        # Right column — outputs
        with gr.Column(scale=1):
            answer_output = gr.Textbox(
                label="🤖 Answer",
                lines=8,
                interactive=False
            )

            sources_output = gr.Textbox(
                label="📚 Source Chunks Used",
                lines=8,
                interactive=False
            )

    # Connect button to function
    ask_button.click(
        fn=build_rag_and_answer,
        inputs=[document_input, question_input],
        outputs=[answer_output, sources_output]
    )

    # Footer
    gr.Markdown("""
    ---
    **Built by [Manpreet Kaur](https://github.com/manuu231)** | 
    MS Data Science @ Clarkson University | 
    Part of 90 Day AI Engineering Journey
    
    🔗 [GitHub](https://github.com/manuu231) | 
    🤗 [Hugging Face](https://huggingface.co/Manpreet02)
    """)

app.launch()

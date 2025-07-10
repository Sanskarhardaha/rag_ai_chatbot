# RAG Chatbot – Legal Document Q&A

## 🔍 Overview
This chatbot answers questions based on legal documents using a RAG (Retrieval-Augmented Generation) pipeline.

## ⚙️ Tech Stack
- 🧠 LLM: Mistral-7B-Instruct
- 📚 Vector Store: FAISS
- ✂️ Chunking: Recursive Character Splitter (300 words, 50 overlap)
- 🔍 Embedding: sentence-transformers/all-MiniLM-L6-v2
- 🖥️ UI: Streamlit with streaming output

## 🏗️ Project Flow
1. Preprocess document into chunks
2. Generate embeddings → store in FAISS
3. Retrieve top chunks for user query
4. Inject context into prompt → generate answer
5. Stream the answer in real-time

## 🚀 Run Locally
```bash
git clone <repo-url>
cd rag-chatbot
pip install -r requirements.txt
streamlit run app.py
```



## 🧪 Sample Queries
- "What is the refund policy?"
- "Is data shared with third parties?"

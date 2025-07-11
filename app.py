import asyncio
import sys
import json
import streamlit as st
from streamlit_lottie import st_lottie
from src.embedder import get_embedder
from src.generator import load_llm
from src.pipeline import generate_answer
from src.retriever import get_chunk_count
from langchain_core.documents import Document
import time

#  Windows async fix
if sys.platform.startswith("win") and sys.version_info >= (3, 8):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

#  Lottie loader
def load_lottie(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

#  Page Setup
st.set_page_config(page_title="🤖 RAG PDF Chatbot", layout="wide")
st.markdown("<h1 style='text-align: center;'> RAG- PDF AI Chatbot </h1>", unsafe_allow_html=True)

#  Two Lottie animations side by side
col1, col2 = st.columns(2)

with col1:
    st_lottie(load_lottie("assets/ai-bot.json"), height=200, key="bot1")

with col2:
    st_lottie(load_lottie("assets/typing-bot.json"), height=200, key="bot2")

#  Load Embedder & LLM
embedder = get_embedder()
llm = load_llm()

#  Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "sources" not in st.session_state:
    st.session_state.sources = []

#  Sidebar
with st.sidebar:
    st.markdown("##  Information")
    st.markdown("**LLM Model:** `Mistral-7B-Instruct`")
    st.markdown(f"**Chunks Indexed:** `{get_chunk_count()}`")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.session_state.sources = []

    if st.button("Download Chat"):
        if st.session_state.messages:
            chat_log = "\n\n".join([f"User: {q}\nBot: {r}" for q, r in st.session_state.messages])
            st.download_button(" Save Chat", chat_log, file_name="chat_history.txt")

#  Input box
query = st.text_input("🔍 Ask a question about the document", placeholder="e.g. List the user policies in bullet points")

#  Handle input
if query:
    with st.spinner("🤖 Thinking..."):
        response, docs = generate_answer(query, embedder, llm)
        st.session_state.messages.append((query, response))
        st.session_state.sources.append(docs)

#  Display chat history with typing animation
if st.session_state.messages:
    for i in range(len(st.session_state.messages) - 1, -1, -1):
        q, r = st.session_state.messages[i]
        docs = st.session_state.sources[i]

        with st.chat_message("user"):
            st.markdown(f"**You:** {q}")

        with st.chat_message("assistant"):
            placeholder = st.empty()
            full_text = ""
            for word in r.split():
                full_text += word + " "
                placeholder.markdown(f"**Bot:** {full_text}▌")
                time.sleep(0.05)
            placeholder.markdown(f"**Bot:** {full_text.strip()}")

            with st.expander("📄 Sources used in this answer"):
                for idx, doc in enumerate(docs):
                    st.markdown(f"**Chunk {idx+1}:**")
                    st.code(doc.page_content.strip(), language="markdown")

else:
    st.info(" Ask a question about the document to begin.")

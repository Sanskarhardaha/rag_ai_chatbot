from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pickle
import os

# ✅ Update this to your actual file name and use raw string for Windows path
loader = PyPDFLoader(r"E:\rag_chatbot_project\data\AI_doc.pdf")
pages = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
chunks = splitter.split_documents(pages)

os.makedirs("chunks", exist_ok=True)
with open("chunks/chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print(f"✅ Done. {len(chunks)} chunks saved to chunks/chunks.pkl.")

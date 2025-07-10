import pickle
from src.embedder import get_embedder
from src.vector_store import build_vector_store

# Load the chunked documents from your 'chunks' folder
with open("chunks/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

# Get embedding model
embedder = get_embedder()

# Build and save the FAISS vector store
build_vector_store(chunks, embedder)

print("✅ Embeddings generated and vector DB saved to vectordb/")

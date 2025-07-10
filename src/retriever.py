from langchain.vectorstores import FAISS

# 🔁 Lazy load FAISS index (with embedder) only once
vectorstore = None

def get_top_k_docs(query, embedder, k=5):
    global vectorstore
    if vectorstore is None:
        vectorstore = FAISS.load_local("vectordb", embeddings=embedder, allow_dangerous_deserialization=True)
    return vectorstore.similarity_search(query, k=k)

def get_chunk_count():
    if vectorstore is not None:
        return len(vectorstore.index_to_docstore_id)
    else:
        # Load only metadata for sidebar if not loaded yet
        dummy = FAISS.load_local("vectordb", embeddings=None, allow_dangerous_deserialization=True)
        return len(dummy.index_to_docstore_id)

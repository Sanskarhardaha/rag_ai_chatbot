from langchain.vectorstores import FAISS

def build_vector_store(chunks, embedding_model):
    db = FAISS.load_local("vectordb", embedder, allow_dangerous_deserialization=True)
    db.save_local("vectordb")

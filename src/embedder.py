from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedder():
    return HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5",
        model_kwargs={"device": "cpu"}  # Required for cloud platforms
    )

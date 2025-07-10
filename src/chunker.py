from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    return splitter.split_documents(docs)

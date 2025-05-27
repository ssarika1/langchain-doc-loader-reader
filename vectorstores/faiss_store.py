from langchain.vectorstores import FAISS
from langchain.schema import Document
from langchain.embeddings import HuggingFaceEmbeddings

def create_faiss_store(documents: list[Document], embeddings: HuggingFaceEmbeddings) -> FAISS:
    return FAISS.from_documents(documents, embeddings)
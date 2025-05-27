from loaders.pdf_loader import load_pdf
from splitters.text_splitter import split_documents
from embeddings.embedding_generator import get_local_embedding_model
from vectorstores.faiss_store import create_faiss_store
from utils.config import CHUNK_SIZE, CHUNK_OVERLAP, EMBEDDING_MODEL

def main():
    file_path = "data/the-great-gatsby.pdf"
    documents = load_pdf(file_path)
    print(f"Loaded {len(documents)} pages from {file_path}")

    split_docs = split_documents(documents, CHUNK_SIZE, CHUNK_OVERLAP)
    print(f"Split into {len(split_docs)} chunks")

    embedding_model = get_local_embedding_model(EMBEDDING_MODEL)
    vectorstore = create_faiss_store(split_docs, embedding_model)

    print("FAISS vector store created with embedded chunks")

if __name__ == "__main__":
    main()
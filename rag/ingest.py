from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from rag.embeddings import embeddings


def process_pdf(
    pdf_path: str,
    tenant_id: str
):

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    # Add source metadata BEFORE splitting
    for doc in documents:
        doc.metadata["source"] = pdf_path

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    vectorstore = Chroma(
        collection_name=f"tenant_{tenant_id}",
        embedding_function=embeddings,
        persist_directory="./chroma_data"
    )

    vectorstore.add_documents(chunks)

    return True
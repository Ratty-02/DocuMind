import os

from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from rag.embeddings import embeddings

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_question(
    tenant_id: str,
    question: str
):

    vectorstore = Chroma(
        collection_name=f"tenant_{tenant_id}",
        embedding_function=embeddings,
        persist_directory="./chroma_data"
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 4}
    )

    docs = retriever.invoke(question)

    # Build sources list
    sources = []

    for doc in docs:
        sources.append(
            {
                "page": doc.metadata.get("page"),
                "source": doc.metadata.get("source")
            }
        )

    # Build context
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are a helpful assistant.

Answer only using the provided context.

Context:
{context}

Question:
{question}
"""
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return {
        "answer": response.content,
        "sources": sources
    }
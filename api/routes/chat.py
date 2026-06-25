from fastapi import APIRouter
from fastapi import Form

from rag.retrieve import ask_question

router = APIRouter()


@router.post("/chat")
def chat(
    tenant_id: str = Form(...),
    question: str = Form(...)
):

    answer = ask_question(
        tenant_id,
        question
    )

    return {
        "answer": answer
    }
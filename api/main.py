from fastapi import FastAPI

from api.routes.upload import router as upload_router
from api.routes.chat import router as chat_router

app = FastAPI(
    title="DocuMind"
)

app.include_router(upload_router)
app.include_router(chat_router)


@app.get("/")
def home():

    return {
        "message": "DocuMind Running"
    }
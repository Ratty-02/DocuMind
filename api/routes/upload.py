import os

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Form

from rag.ingest import process_pdf

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


@router.post("/upload")
async def upload_pdf(
    tenant_id: str = Form(...),
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as f:

        f.write(
            await file.read()
        )

    process_pdf(
        file_path,
        tenant_id
    )

    return {
        "status": "success",
        "tenant_id": tenant_id,
        "file": file.filename
    }
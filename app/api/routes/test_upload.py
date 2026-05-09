# app/api/routes/test_upload.py

from typing import List

from fastapi import APIRouter, UploadFile, File

router = APIRouter()


@router.post("/test-upload")
async def test_upload(
    files: List[UploadFile] = File(...)
):
    return {
        "total_files": len(files)
    }
from fastapi import APIRouter, UploadFile, File, Form
from datetime import datetime


router = APIRouter()

evidence_records = []


@router.post("/investigations/{investigation_id}/upload")
async def upload_log(
    investigation_id: int,
    log_source: str = Form(...),
    file: UploadFile = File(...)
):

    content = await file.read()

    evidence = {
        "id": len(evidence_records) + 1,
        "investigation_id": investigation_id,
        "filename": file.filename,
        "log_source": log_source,
        "size": len(content),
        "uploaded_at": datetime.now()
    }

    evidence_records.append(evidence)

    return {
        "message": "Log uploaded successfully",
        "evidence": evidence
    }


@router.get("/evidence")
def get_evidence():
    return evidence_records
from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlmodel import Session

from app.database.database import get_session
from app.models.evidence import Evidence


router = APIRouter()

evidence_records = []


@router.post("/investigations/{investigation_id}/upload")
async def upload_log(
    investigation_id: int,
    log_source: str = Form(...),
    file: UploadFile = File(...),
    session: Session = Depends(get_session)
):

    upload_path = f"uploads/{file.filename}"

    content = await file.read()

    with open(upload_path, "wb") as f:
        f.write(content)


    evidence = Evidence(
        investigation_id=investigation_id,
        filename=file.filename,
        file_path=upload_path,
        log_source=log_source,
        uploaded_at="now"
    )


    session.add(evidence)
    session.commit()
    session.refresh(evidence)


    return evidence


@router.get("/evidence")
def get_evidence():
    return evidence_records
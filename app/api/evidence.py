from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlmodel import Session

from app.database.database import get_session
from app.models.evidence import Evidence


router = APIRouter(prefix="/evidence",tags=["Evidence"])

evidence_records = []


@router.post("/",
    summary="Upload investigation evidence",
    description="Uploads an authentication log file that will be parsed and analysed.",
    responses={
        201: {"description": "File Uploaded"}}
        
)
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


@router.get("/",
    summary="Get evidence",
    responses={
        200: {"description": "Evidence found"},
        404: {"description": "Evidence not found"}}
)
def get_evidence():
    return evidence_records
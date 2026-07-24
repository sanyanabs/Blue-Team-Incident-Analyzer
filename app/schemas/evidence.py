from sqlmodel import SQLModel


class EvidenceRead(SQLModel):
    id: int
    investigation_id: int
    filename: str
    log_source: str
    uploaded_at: str
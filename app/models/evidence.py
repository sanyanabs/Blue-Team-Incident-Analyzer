from typing import Optional
from sqlmodel import SQLModel, Field


class Evidence(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    investigation_id: int

    filename: str

    file_path: str

    log_source: str

    uploaded_at: str
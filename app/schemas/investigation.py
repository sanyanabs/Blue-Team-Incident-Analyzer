from typing import Optional
from sqlmodel import SQLModel


class InvestigationCreate(SQLModel):
    title: str
    description: Optional[str] = None


class InvestigationRead(SQLModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    severity: str
from typing import Optional
from sqlmodel import SQLModel, Field


class Investigation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    status: str = "Open"
    severity: str = "Unknown"
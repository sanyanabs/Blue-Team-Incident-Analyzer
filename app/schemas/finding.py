from sqlmodel import SQLModel


class FindingRead(SQLModel):
    id: int
    title: str
    severity: str
    description: str
    recommendation: str
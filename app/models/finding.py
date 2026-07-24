from sqlmodel import SQLModel, Field


class Finding(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)

    investigation_id: int

    title: str

    severity: str

    description: str

    impact: str

    recommendation: str

    response_action: str
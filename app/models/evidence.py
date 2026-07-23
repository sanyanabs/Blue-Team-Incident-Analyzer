from datetime import datetime
from pydantic import BaseModel


class Evidence(BaseModel):
    id: int
    investigation_id: int
    filename: str
    log_source: str
    uploaded_at: datetime = datetime.now()
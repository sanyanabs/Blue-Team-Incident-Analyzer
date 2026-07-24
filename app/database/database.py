from sqlmodel import SQLModel, Session, create_engine
from app.models.evidence import Evidence
from app.models.finding import Finding

DATABASE_URL = "sqlite:///blue_team.db"

engine = create_engine(
    DATABASE_URL,
    echo=True
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
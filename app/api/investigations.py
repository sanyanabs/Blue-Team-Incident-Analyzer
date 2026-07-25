from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.database.database import get_session
from app.models.investigation import Investigation
from app.schemas.investigation import (
    InvestigationCreate,
    InvestigationRead
)

router = APIRouter(prefix="/investigations", tags=["Investigations"])

investigations = []

@router.post("/", 
    summary="Create a new investigation",
    description="Creates a new security investigation that will contain uploaded evidence, analysis findings, and generated reports.",
    responses={
    201: {"description": "Investigation created"}}
)
def create_investigation(
    investigation: InvestigationCreate,
    session: Session = Depends(get_session)
):

    db_investigation = Investigation(
        title=investigation.title,
        description=investigation.description
    )

    session.add(db_investigation)
    session.commit()
    session.refresh(db_investigation)

    return db_investigation


@router.get("/",summary="List investigations",
    description="Retrives all investigations.",
    responses={
    200:{"description": "List of investigations retrieved successfully"}}
)
def get_investigations(
    session: Session = Depends(get_session)
):

    return session.exec(
        select(Investigation)
    ).all()


@router.get("/",summary="Retrieve an investigation",
     responses={
     200: {"description": "Investigation found"},
     404: {"description": "Investigation not found"}}
)
def get_investigation(
    investigation_id: int,
    session: Session = Depends(get_session)
):

    investigation = session.get(
        Investigation,
        investigation_id
    )

    if investigation is None:
        raise HTTPException(
            status_code=404,
            detail="Investigation not found"
        )

    return investigation
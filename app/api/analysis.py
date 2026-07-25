from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database.database import get_session
from app.models.evidence import Evidence
from app.models.finding import Finding
from app.parsers.auth_parser import parse_auth_log
from app.detectors.auth_detector import detect_auth_events
from app.models.investigation import Investigation
from app.reports.report_generator import generate_report
from app.reports.pdf_generator import generate_pdf
from fastapi.responses import FileResponse


router = APIRouter(prefix="/analysis",tags=["Analysis"])


@router.post("/",
    summary="Analyse uploaded evidence",
    description="Parses uploaded authentication logs, detects suspicious activities and stores findings.")
def analyze(
    investigation_id: int,
    session: Session = Depends(get_session)
):

    evidence = session.exec(
        select(Evidence)
        .where(
            Evidence.investigation_id == investigation_id
        )
    ).first()


    if not evidence:
        raise HTTPException(
            status_code=404,
            detail="No evidence found"
        )


    events = parse_auth_log(
        evidence.file_path
    )


    findings = detect_auth_events(events)


    saved_findings = []

    for item in findings:

        finding = Finding(
            investigation_id=investigation_id,
            title=item["title"],
            severity=item["severity"],
            description=item["description"],
            impact=item["impact"],
            recommendation=item["recommendation"],
            response_action=item["response_action"]
        )

        session.add(finding)
        saved_findings.append(finding)


    session.commit()


    for finding in saved_findings:
        session.refresh(finding)


    return {
        "message": "Analysis completed",
        "findings": saved_findings
    }

@router.get("/",summary="Retrieve investigation findings")
def get_findings(
    investigation_id: int,
    session: Session = Depends(get_session)
):

    findings = session.exec(
        select(Finding)
        .where(
            Finding.investigation_id == investigation_id
        )
    ).all()


    if not findings:
        raise HTTPException(
            status_code=404,
            detail="No findings found for this investigation"
        )


    return {
        "investigation_id": investigation_id,
        "total_findings": len(findings),
        "findings": findings
    }

@router.get("/",summary="Generate investigation report")
def get_report(
    investigation_id: int,
    session: Session = Depends(get_session)
):

    investigation = session.get(
        Investigation,
        investigation_id
    )


    if not investigation:
        raise HTTPException(
            status_code=404,
            detail="Investigation not found"
        )


    findings = session.exec(
        select(Finding)
        .where(
            Finding.investigation_id == investigation_id
        )
    ).all()


    report = generate_report(
        investigation,
        findings
    )


    return {
        "report": report
    }

@router.get("/",summary="Download investigation report (PDF)")
def download_report_pdf(
    investigation_id: int,
    session: Session = Depends(get_session)
):

    investigation = session.get(
        Investigation,
        investigation_id
    )

    if not investigation:
        raise HTTPException(
            status_code=404,
            detail="Investigation not found"
        )

    findings = session.exec(
        select(Finding)
        .where(
            Finding.investigation_id == investigation_id)
    ).all()

    report = generate_report(
        investigation,
        findings
    )

    pdf_path = f"incident_report_{investigation_id}.pdf"

    generate_pdf(
        report,
        pdf_path
    )

    return FileResponse(
        path=pdf_path,
        media_type="application/pdf",
        filename=f"incident_report_{investigation_id}.pdf"
    )
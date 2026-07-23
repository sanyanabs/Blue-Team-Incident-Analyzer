from fastapi import APIRouter, HTTPException
from app.services.parser import parse_auth_log
from app.services.detection_engine import analyze_events
from app.api.evidence import evidence_records

router = APIRouter()


@router.post("/investigations/{investigation_id}/analyze")
def analyze_investigation(investigation_id: int):

    # Find uploaded evidence
    evidence = next(
        (
            e for e in evidence_records
            if e["investigation_id"] == investigation_id
        ),
        None
    )

    if evidence is None:
        raise HTTPException(
            status_code=404,
            detail="No evidence uploaded for this investigation."
        )

    events = parse_auth_log(evidence["file_path"])

    findings = analyze_events(events)

    return {
        "investigation_id": investigation_id,
        "total_events": len(events),
        "total_findings": len(findings),
        "findings": findings
    }
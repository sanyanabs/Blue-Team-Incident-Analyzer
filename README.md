# Blue-Team-Incident-Analyzer

## Overview

description="""
Blue Team Incident Analyzer is a FastAPI application that automates
the investigation of Linux authentication logs by parsing SSH events,
detecting suspicious activity, generating findings, and exporting
incident reports.

---

## Features

- Create security investigations
- Upload authentication logs
- Parse Linux auth.log files
- Detect:
  - Successful SSH logins
  - Failed login attempts
  - Privileged sudo command execution
- Store findings in SQLite
- Generate investigation reports
- Export reports as PDF
- REST API with Swagger documentation

---

## Technology Stack

- Python 3.11
- FastAPI
- SQLModel
- SQLite
- ReportLab
- Uvicorn

---

## Project Structure

app/
├── api/
├── database/
├── detectors/
├── models/
├── parsers/
├── reports/
├── schemas/
├── main.py

---

## Installation

Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn app.main:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Investigations

POST /investigations/

GET /investigations/

GET /investigations/{id}

### Evidence

POST /evidence/upload

### Analysis

POST /analysis/investigations/{id}/analyze

GET /analysis/investigations/{id}/findings

GET /analysis/investigations/{id}/report

GET /analysis/investigations/{id}/report/pdf

---

## Example Detection

The platform detects events such as:

- Successful SSH logins
- Failed authentication attempts
- Privileged sudo execution

Each event generates:

- Severity
- Description
- Recommendation
- Response Action

---

## Future Improvements

- AI-assisted investigation summaries
- IOC extraction
- MITRE ATT&CK mapping
- Sigma rule generation
- VirusTotal integration
- Threat intelligence enrichment
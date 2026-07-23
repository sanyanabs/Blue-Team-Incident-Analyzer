from fastapi import FastAPI
from app.api import investigations, evidence
from app.api import analyzer
from app.database.database import create_db_and_tables

app = FastAPI(
    title="Blue Team Incident Analyzer",
    description="AI-assisted security log investigation platform",
    version="1.0.0"
)


app.include_router(investigations.router)
app.include_router(evidence.router)
app.include_router(analyzer.router)



@app.get("/")
def health_check():
    return {
        "status": "running",
        "application": "Blue Team Incident Analyzer"
    }
    
@app.on_event("startup")
def on_startup():
    create_db_and_tables()
from fastapi import FastAPI

from app.api import investigations, evidence, analysis
from app.database.database import create_db_and_tables


app = FastAPI(
    title="Blue Team Incident Analyzer",
    description="AI-assisted security log investigation platform",
    version="1.0.0"
)


# Routers MUST come after app creation
app.include_router(investigations.router)
app.include_router(evidence.router)
app.include_router(analysis.router)


@app.get("/")
def health_check():
    return {
        "status": "running",
        "application": "Blue Team Incident Analyzer"
    }


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


print("APP OBJECT:", app)
print("APP ROUTER:", app.router)

print("ANALYSIS ROUTER BEFORE INCLUDE:")
print(analysis.router)

app.include_router(analysis.router)

print("AFTER INCLUDE:")
print("Total routes:", len(app.router.routes))

for route in app.router.routes:
    print(route)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers.upload_report import router as upload_report_router
from backend.routers.upload_prescription import router as upload_prescription_router
from backend.routers.analyze import router as analyze_router
from backend.routers.crosscheck import router as crosscheck_router
from backend.routers.research import router as research_router
from backend.routers.report import router as report_router

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(upload_report_router)
app.include_router(upload_prescription_router)
app.include_router(analyze_router)
app.include_router(crosscheck_router)
app.include_router(research_router)
app.include_router(report_router)

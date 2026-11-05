
import os
from datetime import datetime, timezone

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables
load_dotenv()

# Application Information
APP_NAME = "Mark Analysing Engine"
APP_VERSION = "1.0.0"

# Initialize FastAPI
app = FastAPI(
    title=APP_NAME,
    description="Teacher-Based Academic Mark Management System",
    version=APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Configuration
allowed_origins = [
    origin.strip()
    for origin in os.getenv("FRONTEND_URLS", "*").split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Root Endpoint
@app.get("/")
async def root():
    return {
        "success": True,
        "application": APP_NAME,
        "version": APP_VERSION,
        "message": "Backend is running successfully."
    }


# Health Check Endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "application": APP_NAME,
        "version": APP_VERSION,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


# Application Status Endpoint
@app.get("/api/status")
async def application_status():
    return {
        "success": True,
        "message": "Mark Analysing Engine API is operational.",
        "environment": os.getenv("ENVIRONMENT", "production")
    }

# Desc: Main entry point for the application
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .common.GlobalException.globalexceptionhandler import GlobalExceptionHandler
from app.contoller.task_controller import router as task_router
from app.common.Utils.alert_mapping import AlertMapping
app = FastAPI()
app.exception_handler(Exception)(GlobalExceptionHandler.exception_handler)

# Allow CORS requests from localhost:4200 (Angular app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Angular app URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


@app.on_event("startup")
async def startup_event():
    """Load the message mappings on app startup."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "../Advisor_Alert.xlsx")
    AlertMapping.load_message_mappings(file_path)

# Register routers
app.include_router(task_router, prefix="/api", tags=["Tasks"])

@app.get("/")
def read_root():
    return {"message": "Task Management API is running"}
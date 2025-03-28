from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class EndpointInfo(BaseModel):
    """Schema for API endpoint documentation"""
    path: str
    methods: List[str]
    description: str
    example_request: Optional[dict] = None
    example_response: Optional[dict] = None


class SystemStatus(BaseModel):
    """Standardized health check response"""
    status: str
    service: str
    version: str
    timestamp: datetime
    endpoints: List[EndpointInfo]

    class Config:
        json_schema_extra = {
            "example": {
                "status": "operational",
                "service": "LLM Booking Analytics",
                "version": "1.0.0",
                "timestamp": "2024-03-15T12:00:00Z",
                "endpoints": [
                    {
                        "path": "/ask",
                        "methods": ["POST"],
                        "description": "Submit questions",
                        "example_request": {"question": "What's the cancellation rate?"},
                        "example_response": {"answer": "The rate is 12%", "sources": ["data.csv"]}
                    }
                ]
            }
        }
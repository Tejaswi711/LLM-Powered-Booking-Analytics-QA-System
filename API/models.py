from pydantic import BaseModel
from typing import Optional

class QuestionRequest(BaseModel):
    question: str
    context: Optional[str] = None

class HealthResponse(BaseModel):
    status: str
    services: dict

class AnalyticsResponse(BaseModel):
    status: str
    data: dict

class AnswerResponse(BaseModel):
    status: str
    question: str
    answer: str
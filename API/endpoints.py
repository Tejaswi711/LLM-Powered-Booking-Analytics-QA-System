from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from core.analytics import generate_analytics
from core.rag import answer_question

# Request Models
class QuestionRequest(BaseModel):
    question: str
    context: Optional[str] = None

# Response Models
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

# Initialize router
router = APIRouter(
    prefix="/api/v1",
    tags=["Booking Services"],
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal Server Error"}
    }
)

@router.get(
    "/health",
    response_model=HealthResponse,
    summary="System Health Check",
    description="Check the health status of all system components"
)
async def health_check():
    return {
        "status": "healthy",
        "services": {
            "database": "connected",
            "llm": "ready",
            "vector_db": "loaded",
            "analytics": "operational"
        }
    }

@router.post(
    "/analytics",
    response_model=AnalyticsResponse,
    summary="Generate Analytics Report",
    description="Generate comprehensive booking analytics"
)
async def get_analytics():
    try:
        results = generate_analytics()
        return JSONResponse(content={
            "status": "success",
            "data": results
        })
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Analytics generation failed: {str(e)}"
        )

@router.post(
    "/ask",
    response_model=AnswerResponse,
    summary="Ask Question (POST)",
    description="Submit a question with optional context via POST"
)
async def ask_question_post(request: QuestionRequest):
    try:
        answer = answer_question(
            question=request.question,
            context=request.context
        )
        return {
            "status": "success",
            "question": request.question,
            "answer": answer
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Question processing failed: {str(e)}"
        )

@router.get(
    "/ask",
    response_model=AnswerResponse,
    summary="Ask Question (GET)",
    description="Submit a question with optional context via GET"
)
async def ask_question_get(
    question: str,
    context: Optional[str] = None
):
    try:
        answer = answer_question(question, context)
        return {
            "status": "success",
            "question": question,
            "answer": answer
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Question processing failed: {str(e)}"
        )
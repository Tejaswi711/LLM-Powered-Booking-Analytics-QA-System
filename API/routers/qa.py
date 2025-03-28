from fastapi import APIRouter, HTTPException
from api.models import QuestionRequest, AnswerResponse

router = APIRouter()

@router.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    try:
        # Replace with actual LLM/RAG logic
        return {
            "status": "success",
            "answer": f"Response to: {request.question}",
            "sources": ["policy.pdf"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

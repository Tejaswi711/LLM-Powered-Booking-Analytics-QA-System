from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import os


app = FastAPI(
    title="LLM-Powered Booking Analytics & QA System",
    description="API for booking analytics and question answering",
    version="1.0"
)


class QueryRequest(BaseModel):
    question: str
    user_id: Optional[str] = None

def load_documents():
    print("Loading documents...")

    documents = ["Doc1: Booking Policy", "Doc2: FAQ"]
    print(f"Loaded {len(documents)} documents")
    return documents



documents = []


@app.on_event("startup")
async def startup_event():
    global documents
    documents = load_documents()


@app.get("/")
def home():
    return {
        "message": "LLM Booking Analytics System is running!",
        "endpoints": {
            "/ask": "POST - Submit a question (JSON body: {'question': '...'})",
            "/documents": "GET - List loaded documents"
        }
    }


@app.get("/documents")
def list_documents():
    return {"documents": documents}


@app.post("/ask")
async def ask_question(request: QueryRequest):
    if not request.question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    # Replace with your LLM/QA logic (e.g., call OpenAI, LangChain, etc.)
    mock_response = f"Answer to '{request.question}': Refer to Document 1, Section 3.2."

    return {
        "question": request.question,
        "answer": mock_response,
        "sources": ["Document1"]
    }


# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
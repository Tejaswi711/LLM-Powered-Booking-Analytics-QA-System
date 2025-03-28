from fastapi import FastAPI

app = FastAPI()

# Add this root endpoint
@app.get("/")
async def root():
    return {"message": "Booking Analytics API is running"}

# Your existing endpoints below...
@app.post("/analytics")
async def analytics():
    # Your analytics logic
    return {"data": "Analytics report"}

@app.post("/ask")
async def ask_question(question: str):
    # Your Q&A logic
    return {"answer": "Response to your question"}
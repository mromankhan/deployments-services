from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Progress Service")

class Progress(BaseModel):
    percentage: float

current_progress = {"percentage": 0.0}

@app.get("/progress", response_model=Progress)
async def get_progress():
    return current_progress

@app.post("/progress", response_model=Progress)
async def update_progress(progress: Progress):
    current_progress["percentage"] = progress.percentage
    return current_progress

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

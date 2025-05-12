from fastapi import FastAPI
from app.routers.reviews import router as reviews_router

app = FastAPI(title="GameTracker API")

app.include_router(reviews_router, prefix="/reviews", tags=["reviews"])

@app.get("/")
def read_root():
    return {"message": "Welcome to GameTracker!"}
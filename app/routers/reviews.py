# game-tracker-backend/app/routers/reviews.py
from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import Review, ReviewCreate
from app.crud import create_review, get_reviews

router = APIRouter()

@router.get("/", response_model=List[Review])
def list_reviews():
    return get_reviews()

@router.post("/", response_model=Review)
def add_review(review: ReviewCreate):
    new = create_review(review)
    if not new:
        raise HTTPException(status_code=400, detail="Failed to create review")
    return new

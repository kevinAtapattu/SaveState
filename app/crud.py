# game-tracker-backend/app/crud.py
from typing import List, Dict
from app.db import supabase
from app.schemas import ReviewCreate

def create_review(review: ReviewCreate) -> Dict:
    payload = review.dict()
    res = (
        supabase
        .table("reviews")
        .insert(payload)
        .select("*")
        .execute()
    )
    # res.data is a list of inserted rows
    return res.data[0]

def get_reviews() -> List[Dict]:
    res = supabase.table("reviews").select("*").execute()
    return res.data
    
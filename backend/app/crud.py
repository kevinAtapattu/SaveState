# backend/app/crud.py

from typing import List, Dict, Optional
from fastapi import HTTPException
from app.db import supabase
from app.schemas import ReviewCreate, GameCreate

def create_review(review: ReviewCreate) -> Dict:
    payload = review.dict()
    res = supabase.table("reviews").insert(payload).select("*").execute()
    err = getattr(res, "error", None)
    if err:
        raise HTTPException(status_code=400, detail=err.message)
    data = getattr(res, "data", None)
    if not data:
        raise HTTPException(status_code=500, detail="No review data returned")
    return data[0]

def get_reviews() -> List[Dict]:
    res = supabase.table("reviews").select("*").execute()
    err = getattr(res, "error", None)
    if err:
        raise HTTPException(status_code=400, detail=err.message)
    data = getattr(res, "data", None)
    if data is None:
        raise HTTPException(status_code=500, detail="No reviews data returned")
    return data

def create_game(game: GameCreate) -> Dict:
    payload = game.dict()
    res = supabase.table("games").insert(payload).select("*").execute()
    err = getattr(res, "error", None)
    if err:
        raise HTTPException(status_code=400, detail=err.message)
    data = getattr(res, "data", None)
    if not data:
        raise HTTPException(status_code=500, detail="No game data returned")
    return data[0]

def get_games() -> List[Dict]:
    res = (
        supabase
        .table("games")
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )
    err = getattr(res, "error", None)
    if err:
        raise HTTPException(status_code=400, detail=err.message)
    data = getattr(res, "data", None)
    if data is None:
        raise HTTPException(status_code=500, detail="No games data returned")
    return data

def get_game_by_id(game_id: str) -> Optional[Dict]:
    res = (
        supabase
        .table("games")
        .select("*")
        .eq("id", game_id)
        .single()
        .execute()
    )
    err = getattr(res, "error", None)
    if err:
        raise HTTPException(status_code=400, detail=err.message)
    data = getattr(res, "data", None)
    if data is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return data

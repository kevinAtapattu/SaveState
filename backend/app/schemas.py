# backend/app/schemas.py

from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional, List

# —— Review Schemas ——
class ReviewBase(BaseModel):
    game_id: str
    user_id: str
    rating: float
    comment: Optional[str] = None

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True

# —— Game Schemas ——
class GameBase(BaseModel):
    title: str
    cover_url: Optional[str] = None
    # Use date (YYYY-MM-DD) to match your Postgres column
    release_date: Optional[date] = None

class GameCreate(GameBase):
    pass

class Game(GameBase):
    id: str
    created_at: datetime
    # Optional list of reviews (can be populated later via a join)
    reviews: Optional[List[Review]] = []

    class Config:
        from_attributes = True

# game-tracker-backend/app/schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

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
        orm_mode = True

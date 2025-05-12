# backend/app/routers/games.py

from fastapi import APIRouter, HTTPException
from typing import List

from app.schemas import Game, GameCreate
from app.crud    import create_game, get_games, get_game_by_id

router = APIRouter()

# Handle both /games and /games/
@router.get("",  response_model=List[Game])
@router.get("/", response_model=List[Game])
def list_games():
    return get_games()

@router.post("", response_model=Game)
@router.post("/",response_model=Game)
def add_game(game: GameCreate):
    new = create_game(game)
    if not new:
        raise HTTPException(status_code=400, detail="Failed to create game")
    return new

# Single game by ID (no redirect needed here)
@router.get("/{game_id}", response_model=Game)
def read_game(game_id: str):
    game = get_game_by_id(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game

# backend/main.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

from app.routers.reviews import router as reviews_router
from app.routers.games   import router as games_router

app = FastAPI(title="GameTracker API")

# ── CORS SETUP ───────────────────────────────────────────────────────────────
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ────────────────────────────────────────────────────────────────────────────────

# ── GLOBAL EXCEPTION HANDLER ──────────────────────────────────────────────────
@app.exception_handler(Exception)
async def all_exception_handler(request: Request, exc: Exception):
    import traceback
    tb = traceback.format_exc()
    # return the full traceback for debugging
    return PlainTextResponse(tb, status_code=500)
# ────────────────────────────────────────────────────────────────────────────────

# ── MOUNT ROUTERS ──────────────────────────────────────────────────────────────
app.include_router(reviews_router, prefix="/reviews", tags=["reviews"])
app.include_router(games_router,   prefix="/games",   tags=["games"])
# ────────────────────────────────────────────────────────────────────────────────

@app.get("/")
def read_root():
    return {"message": "Welcome to GameTracker API!"}

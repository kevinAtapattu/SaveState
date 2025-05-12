# game-tracker-backend/app/db.py
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL: str = os.getenv("SUPABASE_URL") or ""
SUPABASE_KEY: str = os.getenv("SUPABASE_KEY") or ""

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

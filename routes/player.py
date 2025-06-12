from fastapi import APIRouter
from config.database import connection_db
from models.player import Player


player_router = APIRouter()

@player_router.get("/")
async def home():
    return "Welcome to the Fullstack Farm"






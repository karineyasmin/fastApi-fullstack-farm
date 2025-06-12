from fastapi import FastAPI
from routes.player import player_router

app = FastAPI()

app.include_router(player_router)
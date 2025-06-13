from fastapi import APIRouter
from config.database import connection_db
from models.player import Player
from schemas.player import entity_player, entity_players_list
from bson import ObjectId


player_router = APIRouter()


@player_router.get("/")
async def home():
    return "Welcome to the Farm Fullstack"


@player_router.get("/players")
async def get_players_list():
    players = connection_db.local.player.find()
    return entity_players_list(players)


@player_router.get("/players/{player_id}")
def get_player_by_id(player_id):
    return entity_player(
        connection_db.local.player.find_one({"_id": ObjectId(player_id)})
    )

@player_router.post("/players")
async def create_player(player: Player):
    connection_db.local.player.insert_one(dict(player))
    return entity_players_list(connection_db.local.jogador.find())

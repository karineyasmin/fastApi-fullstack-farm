def entity_player(db_item) -> dict:
    return {
        "id": str(db_item['_id']),
        "name": db_item["player_name"],
        "age": db_item["player_age"],
        "team": db_item["player_team"]
    }


def entity_players_list(db_item_list) -> list:
    players_list = []
    for item in db_item_list:
        players_list.append(entity_player(item))
    return players_list
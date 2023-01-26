# Variables
gameData = {
    "Player1": {
        "Coins": 0,
        "Coin_Generator": 20,
        "Soliders": []
    },
    "Player2": {
        "Coins": 0,
        "Coin_Generator": 20,
        "Soliders": []
    }
}


def get_status():
    returnData = {
        "first castle health": gameData["Player1"]["Coin_Generator"],
        "first castle soldiers": gameData["Player1"]["Soliders"],
        "second castle health": gameData["Player2"]["Coin_Generator"],
        "second castle soldiers": gameData["Player2"]["Soliders"],
    }
    return returnData

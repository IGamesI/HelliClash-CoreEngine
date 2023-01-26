
# -- Imports
import time

# -- Variables


gameData = {
    "Player1": {
        "Coins": 0,
        "Coin_Generator": 20,
        "Soldiers": []
    },
    "Player2": {
        "Coins": 0,
        "Coin_Generator": 20,
        "Soldiers": []
    }
}
functionsDic = {}

# -- Functions


def get_status():
    returnData = {
        "first castle health": gameData["Player1"]["Coin_Generator"],
        "first castle soldiers": gameData["Player1"]["Soldiers"],
        "second castle health": gameData["Player2"]["Coin_Generator"],
        "second castle soldiers": gameData["Player2"]["Soldiers"],
    }
    return returnData


def teach(team_id, soldier_id):
    if team_id == "first":
        team_id = "Player1"
    elif team_id == "second":
        team_id = "Player2"
    else:
        raise ValueError(
            f"ERR_TeamId: {team_id} is not acceptable, only 'first' and 'second' is defined")

    soldier_id = eval(soldier_id)
    if soldier_id < 2:
        raise ValueError(
            f"ERR_SoliderId: {soldier_id} is not acceptable, only numbers above 1 are acceptable")
    else:
        if gameData[team_id]["Coins"] < soldier_id:
            return False
        else:
            gameData[team_id]["Coins"] -= soldier_id
            gameData[team_id]["Soldiers"].append([soldier_id - 1, 0])
            return True


def add_event(callback, event_id):
    functionsDic[event_id] = callback

# -- Loop


while True:
    # Add coins to player
    gameData["Player1"]["Coins"] += 1
    gameData["Player2"]["Coins"] += 1

    # Move soldiers
    for soldier in gameData["Player1"]["Soldiers"]:
        soldier[1] += 1
    for soldier in gameData["Player2"]["Soldiers"]:
        soldier[1] += 1

    # Wait 1 second
    time.sleep(1)

import json
import random

LOP_FILE = "./LOP/LOP.json"

TEAM_NAMES = ["CSK", "MI", "RCB", "KKR", "DC", "SRH", "GT", "PBKS"]


def load_players():
    with open(LOP_FILE, "r") as f:
        return json.load(f)["players"]


def choose_user_team():
    print("Choose your team:")
    for i, t in enumerate(TEAM_NAMES):
        print(f"{i+1}. {t}")

    choice = int(input("Enter number: ")) - 1
    return TEAM_NAMES[choice]


def create_teams(user_team):
    teams = {}

    for name in TEAM_NAMES:
        teams[name] = {
            "name": name,
            "budget": 100,
            "players": [],
            "is_user": (name == user_team)
        }

    return teams


def main():
    players = load_players()
    random.shuffle(players)

    user_team = choose_user_team()
    teams = create_teams(user_team)

    print(f"\n🎯 You are {user_team}")

    # just test first player
    first = players[0]
    print(f"\nFirst player: {first['name']} ({first['role']}) | {first['base_price']} Cr")


if __name__ == "__main__":
    main()
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


def user_bid(team, player):
    price = player["base_price"]

    print(f"\n🔥 Auction: {player['name']} ({player['role']})")

    while True:
        print(f"\nCurrent Price: {price:.2f} Cr")
        print(f"Your Budget: {team['budget']:.2f} Cr")

        if team["budget"] < price:
            print("❌ Not enough budget")
            return

        choice = input("Bid? (y to bid / n to stop): ").lower()

        if choice == "y":
            price += 0.25
        else:
            if price == player["base_price"]:
                print("❌ Unsold")
                return

            final_price = price - 0.25
            team["players"].append(player)
            team["budget"] -= final_price

            print(f"🏆 Bought {player['name']} for {final_price:.2f} Cr")
            return


def main():
    players = load_players()
    random.shuffle(players)

    user_team = choose_user_team()
    teams = create_teams(user_team)

    print(f"\n🎯 You are {user_team}")

    user_team_obj = teams[user_team]

    # test first 5 players
    for player in players[:5]:
        user_bid(user_team_obj, player)

    print("\n📊 Your Squad:")
    for p in user_team_obj["players"]:
        print(f"- {p['name']} ({p['role']})")

    print(f"\n💰 Remaining Budget: {user_team_obj['budget']:.2f} Cr")


if __name__ == "__main__":
    main()
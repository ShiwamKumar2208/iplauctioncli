import json
import random

LOP_FILE = "./LOP/LOP.json"

TEAMS = [
    {"name": "CSK", "budget": 100, "players": []},
    {"name": "MI", "budget": 100, "players": []},
    {"name": "RCB", "budget": 100, "players": []},
    {"name": "KKR", "budget": 100, "players": []},
    {"name": "DC", "budget": 100, "players": []},
    {"name": "SRH", "budget": 100, "players": []},
    {"name": "GT", "budget": 100, "players": []},
    {"name": "PBKS", "budget": 100, "players": []}
]

MAX_PLAYERS = 25


def load_players():
    with open(LOP_FILE, "r") as f:
        return json.load(f)["players"]


def team_needs_role(team, role):
    count = sum(1 for p in team["players"] if p["role"] == role)

    if role == "Wicketkeeper":
        return count < 1
    if role == "Bowler":
        return count < 4
    if role == "All-Rounder":
        return count < 2

    return True


def decide_bid(team, player, price):
    if team["budget"] < price:
        return False

    if len(team["players"]) >= MAX_PLAYERS:
        return False

    rating = player["rating"]
    demand = player["demand"]

    score = rating + demand + random.randint(-10, 10)

    # role importance boost
    if team_needs_role(team, player["role"]):
        score += 10

    if score > 140:
        return True
    elif score > 120 and price <= 1.5:
        return True
    elif score > 100 and price <= 1.0:
        return True

    return False


def auction_player(player):
    print(f"\n🔥 Auctioning: {player['name']} ({player['role']}) | Base: {player['base_price']} Cr")

    current_price = player["base_price"]
    active_teams = TEAMS.copy()

    while len(active_teams) > 1:
        new_active = []

        for team in active_teams:
            if decide_bid(team, player, current_price):
                print(f"{team['name']} bids {current_price:.2f} Cr")
                new_active.append(team)

        if len(new_active) == 0:
            print("❌ Unsold")
            return

        if len(new_active) == 1:
            winner = new_active[0]
            winner["players"].append(player)
            winner["budget"] -= current_price

            print(f"🏆 SOLD to {winner['name']} for {current_price:.2f} Cr")
            return

        current_price += 0.25
        active_teams = new_active


def main():
    players = load_players()

    # add demand dynamically
    for p in players:
        p["demand"] = random.randint(50, 100)

    print("🏏 IPL AUCTION STARTED\n")

    for player in players:
        auction_player(player)

    print("\n📊 FINAL TEAMS:\n")

    for team in TEAMS:
        print(f"{team['name']} | Budget Left: {team['budget']:.2f} Cr")
        print(f"Players ({len(team['players'])}):")

        for p in team["players"]:
            print(f" - {p['name']} ({p['role']})")

        print("-" * 30)


if __name__ == "__main__":
    main()
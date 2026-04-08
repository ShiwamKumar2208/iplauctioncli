import json
import random
import time
from ai import ai_should_bid
from speaker import speak

LOP_FILE = "./LOP/LOP.json"


def load_players():
    with open(LOP_FILE, "r") as f:
        return json.load(f)["players"]


def create_teams():
    return {
        "SRH": {"name": "SRH", "budget": 100, "players": [], "is_user": True, "strategy": "balanced"},
        "RCB": {"name": "RCB", "budget": 100, "players": [], "is_user": False, "strategy": "aggressive"},
        "CSK": {"name": "CSK", "budget": 100, "players": [], "is_user": False, "strategy": "experienced"},
        "MI": {"name": "MI", "budget": 100, "players": [], "is_user": False, "strategy": "star"},
        "KKR": {"name": "KKR", "budget": 100, "players": [], "is_user": False, "strategy": "allrounder"},
        "DC": {"name": "DC", "budget": 100, "players": [], "is_user": False, "strategy": "youth"},
        "GT": {"name": "GT", "budget": 100, "players": [], "is_user": False, "strategy": "balanced"},
        "PBKS": {"name": "PBKS", "budget": 100, "players": [], "is_user": False, "strategy": "random"}
    }


# 🔥 dynamic increment system
def get_increment(price):
    if price < 5:
        return 0.25
    elif price < 10:
        return 0.5
    else:
        return 1.0


def user_decide(team, player, price):
    print("\n----------------------------------")
    print(f"📢 Auctioneer: {player['name']} ({player['role']})")
    print(f"💰 Current bid: {price:.2f} Cr")
    print(f"🏦 Your purse: {team['budget']:.2f} Cr")

    print("\n👉 Raise the bid?")
    print("(ENTER = No | y = Yes | q = quit)")

    choice = input("Your move: ").strip().lower()

    if choice == "q":
        print("🛑 Auction stopped.")
        exit()

    return choice == "y"


def auction_player(player, teams):
    print("\n==================================")
    print(f"🎤 Auctioneer: {player['name']} coming up!")
    speak(f"{player['name']} coming up for auction")

    print(f"📦 Base price: {player['base_price']} Cr")

    price = player["base_price"]
    leader = None

    # 🔥 OPENING INTEREST
    interested = []

    for t, team in teams.items():
        if team["is_user"]:
            if user_decide(team, player, price):
                interested.append(t)
        else:
            if ai_should_bid(team, player, price, None):
                interested.append(t)

    if not interested:
        print("❌ Unsold")
        speak(f"{player['name']} goes unsold")
        return

    leader = random.choice(interested)

    print(f"🎤 {leader} opens at {price:.2f} Cr!")
    speak(f"{leader} opens bidding at {price:.2f} crores")

    time.sleep(0.3)

    teams_list = list(teams.keys())

    # 🔥 TURN-BASED BIDDING LOOP
    while True:
        increment = get_increment(price)
        next_price = round(price + increment, 2)

        bidders = [t for t in teams_list if t != leader]
        random.shuffle(bidders)

        bid_made = False

        for t in bidders:
            team = teams[t]

            if team["is_user"]:
                bid = user_decide(team, player, next_price)
            else:
                bid = ai_should_bid(team, player, next_price, leader)

            if bid:
                price = next_price
                leader = t
                bid_made = True

                print(f"🗣️ {t} raises to {price:.2f} Cr!")
                speak(f"{t} bids {price:.2f} crores")
                time.sleep(0.25)

                break  # 🔥 ONLY ONE BID PER ROUND

        if not bid_made:
            winner = teams[leader]
            winner["players"].append(player)
            winner["budget"] -= price

            print(f"\n🏆 SOLD to {winner['name']} for {price:.2f} Cr")
            speak(f"{player['name']} sold to {winner['name']} for {price:.2f} crores")
            return


def main():
    players = load_players()
    random.shuffle(players)

    teams = create_teams()

    print("🏏 IPL AUCTION SIMULATOR")
    print("🎯 You are SRH\n")

    for player in players[:15]:  # increase gradually later
        auction_player(player, teams)

    print("\n📊 FINAL TEAMS\n")

    for t in teams.values():
        print(f"{t['name']} | Budget: {t['budget']:.2f}")
        for p in t["players"]:
            print(f" - {p['name']} ({p['role']})")
        print("-" * 30)


if __name__ == "__main__":
    main()



# I want to make a snapshot like tool which will either look or ask for whatever i am using and then save it as a file and when i command the app it will open the exact workspace
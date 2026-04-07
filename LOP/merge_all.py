import json
import os
import random

FILES = ["bat.json", "wk.json", "all.json", "bowl.json"]
OUTPUT_FILE = "LOP.json"


def load_json(file):
    with open(file, "r") as f:
        return json.load(f)


def get_players(data):
    # automatically detect key (batsmen, bowlers, etc.)
    key = list(data.keys())[0]
    return data[key]


def main():
    all_players = []

    print("🔄 Merging files...")

    for file in FILES:
        if not os.path.exists(file):
            print(f"⚠️ {file} not found, skipping.")
            continue

        data = load_json(file)
        players = get_players(data)

        print(f"✔ Loaded {len(players)} players from {file}")

        # ensure all players are dicts
        for p in players:
            if isinstance(p, str):
                all_players.append({"name": p})
            else:
                all_players.append(p)

    print(f"\n📦 Total players before shuffle: {len(all_players)}")

    # shuffle players
    random.shuffle(all_players)

    # assign global id (important for auction)
    for i, player in enumerate(all_players, start=1):
        player["id"] = i

    # save
    with open(OUTPUT_FILE, "w") as f:
        json.dump({"players": all_players}, f, indent=2)

    print(f"✅ Saved merged + shuffled list to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
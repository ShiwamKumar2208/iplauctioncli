import json
import os
import random

FILES = ["bat.json", "wk.json", "all.json", "bowl.json"]
OUTPUT_FILE = "LOP.json"

ROLE_MAP = {
    "bat.json": "Batsman",
    "wk.json": "Wicketkeeper",
    "all.json": "All-Rounder",
    "bowl.json": "Bowler"
}


def load_json(file):
    with open(file, "r") as f:
        return json.load(f)


def get_players(data):
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

        role = ROLE_MAP.get(file, "Unknown")

        print(f"✔ Loaded {len(players)} players from {file} as {role}")

        for p in players:
            if isinstance(p, str):
                player = {"name": p}
            else:
                player = p.copy()

            # 🔥 assign role (overwrite if exists → consistency)
            player["role"] = role

            all_players.append(player)

    print(f"\n📦 Total players before shuffle: {len(all_players)}")

    # shuffle players
    random.shuffle(all_players)

    # assign global ID
    for i, player in enumerate(all_players, start=1):
        player["id"] = i

    # save
    with open(OUTPUT_FILE, "w") as f:
        json.dump({"players": all_players}, f, indent=2)

    print(f"✅ Saved merged + shuffled list to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
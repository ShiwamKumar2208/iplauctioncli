import json
import os

FILES = ["bat.json", "wk.json", "all.json", "bowl.json"]


def load_json(file):
    with open(file, "r") as f:
        return json.load(f)


def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)


def normalize(name):
    return name.strip().lower()


def get_name(player):
    if isinstance(player, str):
        return player
    return player.get("name", "")


def set_name(player, new_name):
    if isinstance(player, str):
        return new_name
    player["name"] = new_name
    return player


def main():
    print("🔥 Duplicate Killer Started")

    all_players = {}
    locations = []

    # Collect all players
    for file in FILES:
        if not os.path.exists(file):
            continue

        data = load_json(file)
        key = list(data.keys())[0]
        players = data[key]

        for idx, player in enumerate(players):
            name = get_name(player)
            norm = normalize(name)

            if norm not in all_players:
                all_players[norm] = []

            all_players[norm].append({
                "file": file,
                "index": idx,
                "name": name
            })

    # Find duplicates
    duplicates = {k: v for k, v in all_players.items() if len(v) > 1}

    if not duplicates:
        print("✅ No duplicates found.")
        return

    print(f"⚠️ Found {len(duplicates)} duplicate groups")

    # Process duplicates
    for norm_name, entries in duplicates.items():
        print("\n==============================")
        print(f"Duplicate: {entries[0]['name']}")

        for i, entry in enumerate(entries):
            print(f"{i}: {entry['name']}  ({entry['file']})")

        keep = input("Which index to KEEP? (number): ")

        if not keep.isdigit():
            print("Skipping...")
            continue

        keep = int(keep)

        for i, entry in enumerate(entries):
            if i == keep:
                continue

            print(f"\n👉 Handling duplicate: {entry['name']} ({entry['file']})")

            action = input("Delete (d), Rename (r), Skip (s): ").lower()

            data = load_json(entry["file"])
            key = list(data.keys())[0]
            players = data[key]

            if action == "d":
                print("Deleting...")
                players[entry["index"]] = None

            elif action == "r":
                new_name = input("Enter new name: ")
                players[entry["index"]] = set_name(players[entry["index"]], new_name)

            elif action == "s":
                print("Skipped.")

            # Remove None entries
            data[key] = [p for p in players if p is not None]

            save_json(entry["file"], data)

    print("\n✅ Duplicate cleanup done!")


if __name__ == "__main__":
    main()
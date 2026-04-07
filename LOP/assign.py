import json
import os

FILES = ["bat.json", "wk.json", "all.json", "bowl.json"]


def load_json(file):
    with open(file, "r") as f:
        return json.load(f)


def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)


def ask_float(prompt, default=None):
    while True:
        val = input(prompt)
        if val == "" and default is not None:
            return default
        try:
            return float(val)
        except ValueError:
            print("Enter a valid number.")


def ask_int(prompt, default=None):
    while True:
        val = input(prompt)
        if val == "" and default is not None:
            return default
        try:
            return int(val)
        except ValueError:
            print("Enter a valid integer.")


def process_file(file):
    print(f"\n=== Processing {file} ===")

    data = load_json(file)

    # Detect key automatically (batsmen, bowlers, etc.)
    key = list(data.keys())[0]
    players = data[key]

    for i, player in enumerate(players):
        # if already processed, skip
        if isinstance(player, dict) and "rating" in player and "base_price" in player:
            continue

        name = player if isinstance(player, str) else player.get("name")

        print(f"\n[{i+1}/{len(players)}] {name}")

        rating = ask_int("Rating (0-100): ")
        base_price = ask_float("Base price (Cr): ")

        # convert to dict if string
        players[i] = {
            "name": name,
            "rating": rating,
            "base_price": base_price
        }

        save_json(file, data)  # save after each entry (safe)

        cont = input("Continue? (Enter to continue, q to quit): ")
        if cont.lower() == "q":
            save_json(file, data)
            print("Progress saved. Exiting.")
            return

    save_json(file, data)
    print(f"Done with {file}!")


def main():
    print("IPL Auction Rating Tool")

    for file in FILES:
        if os.path.exists(file):
            process_file(file)
        else:
            print(f"{file} not found, skipping.")


if __name__ == "__main__":
    main()
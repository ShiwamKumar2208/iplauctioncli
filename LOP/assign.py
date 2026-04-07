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


def get_rating_and_price():
    preset = input("Preset? (e=elite, s=strong, a=avg, u=uncapped, Enter=manual): ").lower()

    if preset == "e":
        return 92, 2.0
    elif preset == "s":
        return 86, 1.5
    elif preset == "a":
        return 80, 1.0
    elif preset == "u":
        return 72, 0.5
    else:
        rating = ask_int("Rating (0-100): ")
        base_price = ask_float("Base price (Cr): ")
        return rating, base_price


def process_file(file):
    print(f"\n=== Processing {file} ===")

    data = load_json(file)

    key = list(data.keys())[0]
    players = data[key]

    for i, player in enumerate(players):
        if isinstance(player, dict) and "rating" in player and "base_price" in player:
            continue

        name = player if isinstance(player, str) else player.get("name")

        print(f"\n[{i+1}/{len(players)}] {name}")

        rating, base_price = get_rating_and_price()

        players[i] = {
            "name": name,
            "rating": rating,
            "base_price": base_price
        }

        save_json(file, data)

        cont = input("Continue? (Enter=yes, q=quit): ").lower()
        if cont == "q":
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
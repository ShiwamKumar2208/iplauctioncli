import random


def calculate_max_price(player):
    rating = player["rating"]
    base = player["base_price"]

    value = rating / 10

    if rating > 90:
        value *= 2.0
    elif rating > 85:
        value *= 1.6
    elif rating > 80:
        value *= 1.3

    return max(value, base * 2)


def ai_should_bid(team, player, price, leader):
    if team["budget"] < price:
        return False

    if leader == team["name"]:
        return False

    rating = player["rating"]
    role = player["role"]
    strategy = team["strategy"]

    max_price = calculate_max_price(player)

    # 🔥 STRATEGY SYSTEM

    if strategy == "aggressive":
        max_price *= 1.4

    elif strategy == "star":
        if rating > 90:
            max_price *= 1.7

    elif strategy == "experienced":
        if rating > 88:
            max_price *= 1.5

    elif strategy == "allrounder":
        if role == "All-Rounder":
            max_price *= 1.6

    elif strategy == "youth":
        if rating < 85:
            max_price *= 1.3

    elif strategy == "random":
        max_price *= random.uniform(0.8, 1.5)

    # 🎲 randomness
    max_price *= random.uniform(0.9, 1.15)

    # 🔥 allow slight overpay
    if price > max_price * 1.1:
        return False

    confidence = rating + random.randint(-12, 12)

    threshold = 85

    return confidence > threshold
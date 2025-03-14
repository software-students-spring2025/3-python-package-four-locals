import random

def flipACoin(num: int) -> list[str]:
    if num <= 0:
        raise ValueError("Number of flips must be greater than zero.")
    return [random.choice(["Heads", "Tails"]) for _ in range(num)]

def rollADice(num: int) -> list[int]:
    if num <= 0:
        raise ValueError("Number of rolls must be greater than zero.")
    return [random.randint(1, 6) for _ in range(num)]

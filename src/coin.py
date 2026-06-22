"""Flip a coin when two options are equally cursed."""

import random
from typing import Literal

Side = Literal["heads", "tails"]


def flip() -> Side:
    """Return heads or tails with equal probability."""
    return random.choice(["heads", "tails"])


def flip_n(count: int) -> list[Side]:
    """Flip `count` coins and return all results."""
    if count < 1:
        raise ValueError("count must be at least 1")
    return [flip() for _ in range(count)]


def best_of(count: int) -> Side:
    """Flip until one side wins a majority of `count` flips."""
    if count < 1 or count % 2 == 0:
        raise ValueError("count must be an odd positive integer")
    needed = count // 2 + 1
    heads = tails = 0
    while heads < needed and tails < needed:
        if flip() == "heads":
            heads += 1
        else:
            tails += 1
    return "heads" if heads > tails else "tails"


if __name__ == "__main__":
    result = flip()
    print(f"The coin says: {result}")
    print("(If you don't like it, that's a you problem.)")

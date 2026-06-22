"""Roll dice when you need chaos more than certainty."""

import random
from typing import Literal

Die = Literal[4, 6, 8, 10, 12, 20]


def roll(sides: Die = 20, count: int = 1) -> list[int]:
    """Roll `count` dice with the given number of sides."""
    if count < 1:
        raise ValueError("count must be at least 1")
    return [random.randint(1, sides) for _ in range(count)]


def roll_with_advantage(sides: Die = 20) -> tuple[int, int, int]:
    """Roll twice, return both rolls and the higher result."""
    first, second = roll(sides, 2)
    return first, second, max(first, second)


def describe_roll(values: list[int]) -> str:
    total = sum(values)
    joined = ", ".join(str(v) for v in values)
    return f"[{joined}] = {total}"


if __name__ == "__main__":
    d20 = roll(20)
    adv = roll_with_advantage(20)
    print(f"Single d20: {describe_roll(d20)}")
    print(f"Advantage: rolled {adv[0]} and {adv[1]} -> kept {adv[2]}")

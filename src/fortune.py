"""A totally unnecessary fortune cookie generator."""

import random
from datetime import datetime

FORTUNES = [
    "Your next commit will pass CI on the first try.",
    "A merge conflict lurks in your near future — stay calm.",
    "The bug you fear is not in prod. Yet.",
    "Today is a good day to refactor that one function.",
    "Someone will approve your PR before lunch.",
    "The linter and you will become friends.",
    "Your coffee and your code will both compile.",
    "A wild feature request appears — choose wisely.",
]


def pick_fortune() -> str:
    """Return a random fortune string."""
    return random.choice(FORTUNES)


def fortune_with_timestamp() -> dict:
    """Return a fortune bundled with metadata."""
    return {
        "fortune": pick_fortune(),
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "lucky_number": random.randint(1, 99),
    }


if __name__ == "__main__":
    result = fortune_with_timestamp()
    print(f"🥠 {result['fortune']}")
    print(f"Lucky number: {result['lucky_number']}")

"""Ask the magic 8-ball when you need an answer faster than a standup."""

import random

RESPONSES = [
    "It is certain.",
    "Reply hazy, try again.",
    "Don't count on it.",
    "Yes — and write a test for it.",
    "Cannot predict now. Check the logs.",
    "Outlook good, but add error handling.",
    "My sources say no. Have you tried turning it off and on again?",
    "Signs point to yes. Ship it.",
    "Very doubtful. Read the docs first.",
    "As I see it, yes — but only on staging.",
]


def ask(question: str) -> str:
    """Return a mystical answer to any yes/no question."""
    if not question.strip():
        raise ValueError("You must ask a question.")
    return random.choice(RESPONSES)


def main() -> None:
    question = input("Ask the 8-ball: ")
    print(f"\n🎱 {ask(question)}")


if __name__ == "__main__":
    main()

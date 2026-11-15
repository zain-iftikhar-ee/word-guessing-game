"""Word Guessing Game — guess the hidden word letter by letter.

Run:  python3 word_guessing.py
"""

import random

WORDS = [
    "python", "computer", "laptop", "keyboard", "program",
    "science", "engineer", "circuit", "voltage", "battery",
    "inverter", "solar", "project", "student", "lahore",
]


def play_round(word, max_attempts=6):
    """Play one round. Returns True if the player guessed the word."""
    guessed = set()
    attempts = max_attempts
    while attempts > 0:
        display = " ".join(c if c in guessed else "_" for c in word)
        print(f"\nWord: {display}")
        print(f"Guessed letters: {', '.join(sorted(guessed)) or 'none'}")
        print(f"Attempts left: {attempts}")
        letter = input("Guess a letter: ").strip().lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter.")
            continue
        if letter in guessed:
            print("You already guessed that letter.")
            continue
        guessed.add(letter)
        if letter in word:
            print(f"Good! '{letter}' is in the word.")
            if all(c in guessed for c in word):
                print(f"\nYou guessed it! The word was '{word}'.")
                return True
        else:
            attempts -= 1
            print(f"Sorry, '{letter}' is not in the word.")
    print(f"\nOut of attempts! The word was '{word}'.")
    return False


def main():
    print("Word Guessing Game — guess the hidden word!")
    wins = losses = 0
    while True:
        word = random.choice(WORDS)
        if play_round(word):
            wins += 1
        else:
            losses += 1
        print(f"Score — Won {wins} | Lost {losses}")
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            break
    print("Thanks for playing!")


if __name__ == "__main__":
    main()

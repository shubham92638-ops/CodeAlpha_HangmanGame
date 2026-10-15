# TASK 1: Hangman Game

A simple, text-based Hangman game created in Python where players guess a secret word one letter at a time.

## Features
- **Predefined Word List**: 5 predefined words (`python`, `coding`, `software`, `keyboard`, `puzzle`).
- **Attempts Limit**: Players can make up to 6 incorrect guesses before the game ends.
- **Input Validation**: Rejects invalid inputs (numbers, symbols, multiple letters) and prevents duplicate guesses without penalty.
- **Pure Console I/O**: Clean text interface with no graphics or external dependencies required.

## Key Concepts Used
- **`random` module**: `random.choice()` selects a secret word randomly from the list.
- **`while` loop**: Keeps the game active until either the word is solved or 6 incorrect guesses are reached.
- **`if-else` conditionals**: Handles letter validation, checking hits vs. misses, and win/loss conditions.
- **Strings**: String manipulation and formatting (`.lower()`, `.strip()`, `.isalpha()`, `.join()`).
- **Lists**: Used for storing the predefined word bank, letter tracking, and building the masked display word.

## How to Run

1. Open your terminal in this directory.
2. Run the game with:
   ```bash
   python hangman.py
   ```

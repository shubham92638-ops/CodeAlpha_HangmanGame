import random


def play_hangman():
    # Predefined list of 5 words
    words = ["python", "coding", "software", "keyboard", "puzzle"]

    # Randomly select a secret word
    secret_word = random.choice(words)

    # Tracking guesses
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("=" * 36)
    print("      WELCOME TO HANGMAN GAME       ")
    print("=" * 36)
    print(f"Guess the word one letter at a time.")
    print(f"You are allowed a maximum of {max_incorrect_guesses} incorrect guesses.\n")

    # Main game loop
    while incorrect_guesses < max_incorrect_guesses:
        # Build the current displayed word
        display_word = []
        for letter in secret_word:
            if letter in guessed_letters:
                display_word.append(letter)
            else:
                display_word.append("_")

        # Print current game status
        print("Word:", " ".join(display_word))
        print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        # Check if user has guessed all letters
        if "_" not in display_word:
            print("\n Congratulations! You guessed the word correctly!")
            print(f"The word was: {secret_word}")
            break

        # Get user input
        guess = input("\nEnter a letter: ").strip().lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print(">> Invalid input. Please enter a single alphabetic letter.\n")
            continue

        if guess in guessed_letters:
            print(f">> You already guessed '{guess}'. Try a different letter.\n")
            continue

        # Add guess to history
        guessed_letters.append(guess)

        # Check if the guess is in the secret word
        if guess in secret_word:
            print(f">> Good job! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            remaining = max_incorrect_guesses - incorrect_guesses
            print(f">> Sorry, '{guess}' is not in the word. ({remaining} attempts remaining)\n")

    # End of game check when max incorrect guesses reached
    if incorrect_guesses >= max_incorrect_guesses:
        print("=" * 36)
        print("GAME OVER! You ran out of guesses.")
        print(f"The secret word was: '{secret_word}'")
        print("=" * 36)


if __name__ == "__main__":
    play_hangman()

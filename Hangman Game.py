import random

# Define stages and alphabet globally
stages = [
    """
        --------
        |      |
        |
        |
        |
        |
        -------
    """,
    """
        --------
        |      |
        |      O
        |
        |
        |
        -------
    """,
    """
        --------
        |      |
        |      O
        |      |
        |
        |
        -------
    """,
    """
        --------
        |      |
        |      O
        |     /|
        |
        |
        -------
    """,
    """
        --------
        |      |
        |      O
        |     /|\\
        |
        |
        -------
    """,
    """
        --------
        |      |
        |      O
        |     /|\\
        |     /
        |
        -------
    """,
    """
        --------
        |      |
        |      O
        |     /|\\
        |     / \\
        |
        -------
    """
]

alphabet = set('abcdefghijklmnopqrstuvwxyz')

def choose_word():
    """Chooses a random word from a list of words."""
    words = ["priyanka","pawar","pratiksha"]
    while True:  # Loop until a non-empty word is chosen
        word = random.choice(words)
        if len(word) > 0:  # Check if the chosen word is not empty
            return word

def display_hangman(wrong_guesses):
    """Displays the hangman figure based on the number of wrong guesses."""
    return stages[wrong_guesses]

def play_hangman():
    """Main function that plays the Hangman game."""
    word = choose_word()
    word_letters = set(word)  # Convert the word to a set of unique letters
    wrong_guesses = 0
    guessed_letters = set()

    print("Welcome to Hangman!")
    print(display_hangman(wrong_guesses))

    while wrong_guesses < len(stages) - 1:
        print("You have", len(alphabet), "letters left to guess.")
        print("Used letters:", ' '.join(guessed_letters))

        # Show the word with placeholders for unguessed letters
        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(word_display))

        guess = input("Guess a letter: ").lower()

        if guess in alphabet:
            guessed_letters.add(guess)
            if guess not in word_letters:
                wrong_guesses += 1
                print("Wrong guess!")
            else:
                print("Good guess!")
                # Check if all letters are guessed
                if all(letter in guessed_letters for letter in word_letters):
                    print(f"You win! The word was {word}.")
                    break
        else:
            print("Invalid input, please enter a single letter.")

        print(display_hangman(wrong_guesses))

    if wrong_guesses == len(stages) - 1:
        print(f"You lose! The word was {word}.")

# Start the game
play_hangman()

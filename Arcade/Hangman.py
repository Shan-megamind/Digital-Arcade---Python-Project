from random_word import RandomWords

# Hangman Stages in the form of stick figures 
hangman_stages = [
    """
     ------
     |    |
     |
     |
     |
     |
    ------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    ------
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    ------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    ------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ------
    """
]

# Function to generate random meaningful word
def generate_random_word():
    r = RandomWords()
    word = r.get_random_word()
    if word:
        return word.lower()
    else:
        return "arivederci"  # In case no word is generated

# Function to display current progress of the word
def display_current_progress(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Main Hangman Code - Where Magic Happens
def hangman():
    word = generate_random_word()  # Calling the function to get a random meaningful word
    guessed_letters = set()
    remaining_attempts = len(hangman_stages) - 1  # Number of stages left before 'Game Over'
    word_guessed = False
    guess_count = 0

    print("Welcome to Hangman")
    print("Try to guess the Word, one letter at a time")
    print("The life of this man..")
    print(
        """ 
          o/
         /|
         / \\
        """
    )
    print("Is in your hands!")
    print(f"You have {remaining_attempts} attempts to guess the word")

    # Game working
    while remaining_attempts > 0 and not word_guessed:
        # Displaying Hangman stage, Current word progress, and number of attempts remaining
        print("\n" + hangman_stages[len(hangman_stages) - 1 - remaining_attempts])
        print("Word: ", display_current_progress(word, guessed_letters))
        print(f"Number of letters in the word: {len(word)}")
        print("Number of attempts: ", remaining_attempts)
        print("Guessed letters:", " ".join(sorted(guessed_letters)))  # Displaying guessed letters in alphabetical order for clarity

        guess = input("Guess a letter: ").lower()
           
        # Input Validation: Length and character
        if len(guess) != 1 or not guess.isalpha():
            print("What are you doing? Please enter a single letter!")
            continue  # Skips the rest of the code and restarts

        # Input Validation: If letter was already guessed
        if guess in guessed_letters:
            print(f"You've already guessed {guess}. Concentrate!")
            continue

        guessed_letters.add(guess)

        # Check if guess is correct 
        if guess in word:
            print(f"Awesome! '{guess}' is in the word")
        else:
            print(f"NO! '{guess}' is not in the word")
            remaining_attempts -= 1
        
        # Check if the word is guessed 
        word_guessed = all(letter in guessed_letters for letter in word)
        
    # Final Result 
    if word_guessed:
        print(f"\nCongratulations! You have correctly guessed the word, '{word}'")
        print("You have saved him!")
        print(
                    """
                    \ o /
                      |
                     / \  
                """
            )
    else:
        print(hangman_stages[-1])  # Showing the final Hangman stage
        print("Alas! You couldn't save him. He's dead because of you")
        print(f"The word was '{word}'")

# Start the Game!!!
def start_game():
    hangman()

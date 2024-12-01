# Import the games from respective modules
from RockPaperScissor import start_game as rps_game
from Hangman import start_game as hangman_game
from Blackjack import start_game as blackjack_game

class DigitalArcade:
    def __init__(self):
        # initializing the aracde with a dictionary of games | Each entry maps a number corresponding to the game and its start function
        self.games = {
            "1": ("Rock-Paper-Scissors", rps_game),
            "2": ("Hangman", hangman_game),
            "3": ("Blackjack", blackjack_game),
        }

    # Display the main menu 
    def display_menu(self):
        print("""
       ╔════════════════════════════════════╗
       ║    Welcome to Megamind's Arcade!   ║
       ║ Buckle up for some Exciting Games  ║
       ╚════════════════════════════════════╝
    """)
        print("\nChoose a game to play:")
        # Iterate through the available games and display their names and descriptions
        for key, (name, _) in self.games.items():
            description = self.game_description(name)
            print(f"{key}. {name} - {description}") # Games and thier respective descriptions
        print("Q. Quit")

    # Function to add short descriptions to the games
    def game_description(self, name):
        descriptions = {
            "Rock-Paper-Scissors": "Classic game of strategy. First to 5 points wins!",
            "Hangman": "Guess the word before the stickman meets his end.",
            "Blackjack": "Beat the dealer without exceeding 21!",
        }
        # Return description or default if not found
        return descriptions.get(name, "A fun game!")

    # Function to play the selected game
    def play_game(self, game_function):
        while True:
            game_function() # Launch the game using its start function
            # Ask the player if they want to replay, return to the menu, or quit
            replay_choice = input ("\nWould you like to replay this game (R), return to the main menu (M), or quit the arcade (Q)? ").strip().upper()
            if replay_choice == "R":
                print("\nRestarting the game...\n")
                continue
            elif replay_choice == "M":
                print("\nReturning to the Main Menu...\n")
                break
            elif replay_choice == "Q":
                print("\nBOOOOOORIIIIINNNGGGG! Thanks for visiting Megamind's Digital Arcade! Goodbye!")
                exit()
            else:
                print("Invalid choice! Select R, M, or Q.")

    # Main loop to display the main menu and handle user choices
    def play(self):
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1/2/3/Q): ").strip().upper()
            if choice == "Q":
                print("\nBOOOOOORIIIIINNNGGGG! Thanks for visiting Megamind's Digital Arcade! Goodbye!")
                break
            elif choice in self.games:
                game_name, game_function = self.games[choice]
                print(f"\nLaunching {game_name}...\n")
                self.play_game(game_function) 
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    arcade = DigitalArcade()
    arcade.play()

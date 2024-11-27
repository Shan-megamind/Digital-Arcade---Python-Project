# Import the games
from RockPaperScissor import start_game as rps_game
from Hangman import start_game as hangman_game
from Blackjack import start_game as blackjack_game

class DigitalArcade:
    def __init__(self):
        self.games = {
            "1": ("Rock-Paper-Scissors", rps_game),
            "2": ("Hangman", hangman_game),
            "3": ("Blackjack", blackjack_game),
        }

    def display_menu(self):
        print("\nWelcome to Megamind's Digital Arcade!")
        print("I am Megamind and I have three games for you to play!")
        print("\nChoose a game to play:")
        for key, (name, _) in self.games.items():
            print(f"{key}. {name}")
        print("Q. Quit")

    def play(self):
        while True:
            self.display_menu()
            choice = input("\nEnter your choice: ").strip().upper()
            if choice == "Q":
                print("\nBOOOOOORIIIIINNNGGGG! Thanks for visiting Megamind's Digital Arcade! Goodbye!")
                break
            elif choice in self.games:
                game_name, game_function = self.games[choice]
                print(f"\nLaunching {game_name}...\n")
                game_function()
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    arcade = DigitalArcade()
    arcade.play()
import random

# Rock Paper Scissor options picked through the dictionary
weapon_art = {
    "r": """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    "p": """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
    "s": """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
}

# How is the winner decided
def winner_decider(player, computer):
    if player == computer:
        return "tie"
    elif (player == "r" and computer == "s") or \
         (player == "s" and computer == "p") or \
         (player == "p" and computer == "r"):
        return "player"
    else:
        return "computer"

# The actual game : Where Magic Happens
def rock_paper_scissors():
    #while True:
     print("\nWelcome to the Classic: Rock, Paper, Scissors!")
     print("It is You vs Me")
     print("First to get to 5 points, WINS!")
     print("Prepare to lose!")

     player_score = 0
     computer_score = 0

     while player_score < 5 and computer_score < 5:
        print("\nChoose your option: rock (r), paper (p), or scissors (s)")
        player_choice = input("You choose: ").lower()

        # Check for valid input 
        if player_choice not in ["r", "p", "s"]:
            print("Invalid choice! I see you are nervous!")
            print("Please choose one of these: r, p, or s")
            continue

        # Generate random computer choice
        computer_choice = random.choice(["r", "p", "s"])

        # Display choices from the above set dictionary art
        print("\nYou Chose:")
        print(weapon_art[player_choice])
        print("I Chose: ")
        print(weapon_art[computer_choice])

        # Deciding the winner 
        result = winner_decider(player_choice, computer_choice)

        if result == "tie":
            print("It's a tie! No points for anyone!")
        elif result == "player":
            print("Huh! You win this round!")
            player_score += 1
        else:
            print("Haha! I win this round!")
            computer_score += 1

        # Score display
        print(f"\nCurrent Scores: You: {player_score} | Me: {computer_score} ")
    
     # Getting the final winner
     if player_score == 5:
        print("\nCongratulations! I am defeated. You've reached 5 points first and WON THE GAME!")
     else:
        print("\nHAHA! You have been defeated! I've reached 5 points first, and WON THE GAME!")
        print("Better Luck Next time!")
     
     #replay = input("\nWould you like to play again? (yes/no): ").lower()
     #if replay != "yes":
      #   print("Thanks for playing! Later Skater!")
       #  break

# Start the game 
def start_game():
    rock_paper_scissors()

import random

# Rock Paper Scissor options picked through the dictionary
weapon_art = {
    "rock": """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    "paper": """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
    "scissors": """
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
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

# The actual game : Where Magic Happens
def rock_paper_scissors():
    print("\nWelcome to the Classic: Rock, Paper, Scissors!")
    print("It is You vs Me")
    print("First to get to 5 points, WINS!")
    print("Prepare to lose!")

    player_score = 0
    computer_score = 0

    while player_score < 5 and computer_score < 5:
        print("\nChoose your option: rock, paper, or scissors")
        player_choice = input("You choose: ").lower()

        # Check for valid input 
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! I see you are nervous!")
            print("Please choose one of these: rock, paper, or scissors")
            continue

        # Generate random computer choice
        computer_choice = random.choice(["rock", "paper", "scissors"])

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

# Start the game 
rock_paper_scissors()
import random

# Card values
CARD_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11  # Ace can be 1 or 11
}

# Generate a deck of cards
def create_deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    cards = list(CARD_VALUES.keys())
    deck = [f"{card} of {suit}" for card in cards for suit in suits]
    random.shuffle(deck)
    return deck

# Calculate hand value
def calculate_hand(hand):
    value = 0
    aces = 0
    for card in hand:
        card_value = card.split(" ")[0]  # Extract card value
        value += CARD_VALUES[card_value]
        if card_value == "A":
            aces += 1
    # Adjust for Aces if value > 21
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1
    return value

# Display hand with ASCII art
def display_hand_with_art(hand, hide_first_card = False):
    def card_art(card):
        suit_symbols = {"Hearts": "♥", "Diamonds": "♦", "Clubs": "♣", "Spades": "♠"}
        value, suit = card.split(" ")[0], card.split(" ")[2]
        symbol = suit_symbols[suit]
        return [
            "┌─────────┐",
            f"│{value:<2}       │",  # Top-left value
            "│         │",
            f"│    {symbol}    │",  # Suit symbol in the middle
            "│         │",
            f"│       {value:>2}│",  # Bottom-right value
            "└─────────┘"
        ]

    # Hide the first card if needed
    if hide_first_card:
        hand = ["Hidden"] + hand[1:]

    # Generate ASCII art for each card
    all_cards_art = [card_art(card) if card != "Hidden" else [
        "┌─────────┐",
        "│░░░░░░░░░│",
        "│░░░░░░░░░│",
        "│░░Hidden░│",
        "│░░░░░░░░░│",
        "│░░░░░░░░░│",
        "└─────────┘"
    ] for card in hand]

    # Print ASCII art line by line
    for i in range(7):  # Each card has 7 lines
        print("  ".join(card[i] for card in all_cards_art))

# Quick rule guide
def display_rules():
    print("""
Welcome to Blackjack!
======================
- The goal is to get as close to 21 as possible without exceeding it.
- Number cards are worth their face value.
- Face cards (J, Q, K) are worth 10.
- Aces (A) can be 1 or 11, whichever helps you most.
- Actions:
  - Hit: Draw another card.
  - Stand: Keep your current hand and end your turn.
======================
""")

# Main game loop
def blackjack():
    display_rules()
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("\nDealer's Hand:")
    display_hand_with_art(dealer_hand, hide_first_card = True)
    print("\nYour Hand:")
    display_hand_with_art(player_hand)

    # Player's turn
    while calculate_hand(player_hand) < 21:
        choice = input("\nDo you want to [H]it or [S]tand? ").upper()
        if choice == "H":
            player_hand.append(deck.pop())
            print("\nYour Hand:")
            display_hand_with_art(player_hand)
            if calculate_hand(player_hand) > 21:
                print("\nYou busted!")
                return
        elif choice == "S":
            break

    # Dealer's turn
    print("\nDealer's Turn:")
    print("\nDealer's Hand:")
    display_hand_with_art(dealer_hand)
    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        print("\nDealer draws a card. Dealer's Hand:")
        display_hand_with_art(dealer_hand)
        if calculate_hand(dealer_hand) > 21:
            print("\nDealer busted! You win!")
            return

    # Final results
    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)
    print(f"\nYour Total: {player_total}")
    print(f"Dealer's Total: {dealer_total}")

    if player_total > dealer_total:
        print("\nYou win!")
    elif player_total < dealer_total:
        print("\nDealer wins!")
    else:
        print("\nIt's a tie!")

# Run the game
def start_game():
    if __name__ == "__main__":
        blackjack()


import random

def deal_card():
    """Deal a random card."""
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

def calculate_score(cards):
    """Calculate the total score of a hand of cards."""
    score = 0
    num_aces = 0
    for card in cards:
        if card.isdigit():
            score += int(card)
        elif card in ['J', 'Q', 'K']:
            score += 10
        elif card == 'A':
            num_aces += 1
            score += 11
    # Adjust for aces if needed
    while score > 21 and num_aces:
        score -= 10
        num_aces -= 1
    return score

def blackjack():
    print("Welcome to Blackjack!")
    player_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]

    print("Your cards:", player_cards)
    print("Dealer's card:", dealer_cards[0])

    # Player's turn
    while True:
        player_score = calculate_score(player_cards)
        if player_score == 21:
            print("Blackjack! You win!")
            return
        elif player_score > 21:
            print("Busted! You lose.")
            return

        action = input("Do you want to hit or stand? (h/s): ")
        if action == 'h':
            player_cards.append(deal_card())
            print("Your cards:", player_cards)
        elif action == 's':
            break

    # Dealer's turn
    print("Dealer's cards:", dealer_cards)
    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(deal_card())
        print("Dealer hits. Dealer's cards:", dealer_cards)

    dealer_score = calculate_score(dealer_cards)
    if dealer_score > 21:
        print("Dealer busted! You win!")
    elif dealer_score == player_score:
        print("It's a tie!")
    elif dealer_score > player_score:
        print("Dealer wins!")
    else:
        print("You win!")

blackjack()
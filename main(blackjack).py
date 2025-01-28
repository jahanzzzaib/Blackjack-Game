import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the sum of the list"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Its a Draw :)"
    elif computer_score == 0:
        return "You lost :( Computer has Blackjack"
    elif user_score == 0:
        return "You win by Blackjack!"
    elif user_score > 21:
        return "You went over, you lose :("
    elif computer_score > 21:
        return "Computer went over, you win!"
    elif user_score > computer_score:
        return "You win!"
    elif computer_score > user_score:
        return "You lose :("

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    sum_user = calculate_score(user_cards)
    sum_computer = calculate_score(computer_cards)
    game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        sum_user = calculate_score(user_cards)
        sum_computer = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, Current score: {sum_user}")
        print(f"Computers first card: {computer_cards[0]}")

        if sum_user == 0 or sum_computer == 0 or sum_user > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while sum_computer != 0 and sum_computer < 17:
        computer_cards.append(deal_card())
        sum_computer = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, Final score: {sum_user}")
    print(f"Computers final hand: {computer_cards}, Final score: {sum_computer}")
    print(compare(sum_user,sum_computer))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
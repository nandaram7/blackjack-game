import random
from art import logo

# variable definitions
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# function definitions
def choose_card():
    """Gets an index to choose a random card"""
    return random.randint(0, 12)

def add_cards(card_list):
    """Basic level function to sum(card_list) with Ace to act as 1 or 11"""
    total = 0
    for card in card_list:
        total += card
        if card == 11 and total > 21:
            total -= 10
    return total

def dealing_card():
    """Deals card to the customer as long as they want to continue"""
    continue_deal = input("Type 'y' to get another card and get 'n' to pass: ")
    if continue_deal == 'y':
        user_list.append(cards[choose_card()])
        total = add_cards(user_list)
        if total > 21:
            return

        print(f"\tYour cards: {user_list}, current score: {total}")
        print(f"\tComputer's first card is {computer_list[0]}")
        dealing_card()

    elif continue_deal != 'n':
        print("Don't be oversmart weirdo!")
        dealing_card()
    else:
        return

def computer_deal():
    """Gets cards for the computer when the user has chosen to stand"""
    computer_list.append(cards[choose_card()])
    total = add_cards(computer_list)
    if total < 17:
        computer_deal()
    else:
        return

def final_result(u_total, c_total):
    if u_total == c_total:
        return "Thats a Drawww"
    elif c_total == 21:
        return "Computer's got a BLACKJACK. You lose!!!"
    elif u_total == 21:
        return "You win with a BLACKJACK!!!"
    elif u_total > 21:
        return "You went over! You lose!!!"
    elif c_total > 21:
        return "Computer went over! You win!!!"
    elif c_total > u_total:
        return "You lose!!!"
    else:
        return "You win!!! Wooohoooo!!!"

# Main BLACKJACK LOOP
while 1:
    user_list = []
    computer_list = []
    # Loop continue?
    user_choice = input("Welcome to the BLACKJACK game. Would you like to play? Type 'y' or 'n': ")
    if user_choice == 'n':
        break
    elif user_choice == 'y':
        print("\n"*20)
        print(logo)
    else:
        print("Lets try that again huh??? \n\n")
        continue

    # Customer and computer first deal
    for _ in range(2):
        user_list.append(cards[choose_card()])
        computer_list.append(cards[choose_card()])
    
    user_total = add_cards(user_list)
    computer_total = add_cards(computer_list)
    print(f"\tYour cards: {user_list}, current score: {user_total}")
    print(f"\tComputer's first card: {computer_total}")

    if computer_total != 21 or user_total != 21:
        dealing_card()

    if computer_total != 21 or user_total != 21:
        computer_deal()

    user_total = add_cards(user_list)
    computer_total = add_cards(computer_list)
    print(f"\tYour final hand: {user_list}, final score: {user_total}")
    print(f"\tComputer's final hand: {computer_list}, final score: {computer_total}\n")
    print(final_result(user_total, computer_total))

import random
from art import logo

# variable definitions

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
loop_continue = True

# function definitions
def choose_card():
    return random.randint(0, 12)

def add_cards(card_list):
    total = 0
    for card in card_list:
        total += card
        if card == 11 and total > 21:
            total -= 10
    return total

def dealing_card():
    continue_deal = input("Type 'y' to get another card and get 'n' to pass: ")
    if continue_deal == 'y':
        user_list.append(cards[choose_card()])
        total = add_cards(user_list)
        if total > 21:
            return

        print(f"\tYour cards: {user_list}, current score: {total}")
        print(f"\tComputer's first card is {computer_total}")
        dealing_card()

    elif continue_deal != 'n':
        print("Don't be oversmart weirdo!")
        dealing_card()
    else:
        return

def computer_deal():
    computer_list.append(cards[choose_card()])
    total = add_cards(computer_list)
    if total < 17:
        computer_deal()
    else:
        return

def final_score():
    print(f"\tYour final hand: {user_list}, final score: {user_total}")
    print(f"\tComputer's final hand: {computer_list}, final score: {computer_total}\n")

# Main BLACKJACK LOOP
while loop_continue:
    # Loop continue?
    user_choice = input("Welcome to the BLACKJACK game. \nWould you like to play? Type 'y' or 'n': ")
    if user_choice == 'n':
        break
    elif user_choice == 'y':
        print("\n"*20)
        print(logo)
    else:
        print("Lets try that again huh??? \n\n")
        continue

    # Customer first deal
    user_list = [cards[choose_card()], cards[choose_card()]]
    user_total = add_cards(user_list)
    # Computer first card
    computer_list = [cards[choose_card()]]
    computer_total = add_cards(computer_list)

    print(f"\tYour cards: {user_list}, current score: {user_total}")
    print(f"\tComputer's first card: {computer_total}")

    if user_total == 21:
        final_score()
        print("That's a perfect hand! You win with a BLACKJACK!\n")
        break

    dealing_card()
    user_total = add_cards(user_list)
    if user_total > 21:
        final_score()
        print("You went over! You lose!\n")

    else:
        computer_deal()
        computer_total = add_cards(computer_list)
        final_score()

        if computer_total > 21:
            print("Computer went over! You win!\n")
        else:
            if computer_total > user_total:
                print("Computer has won!\n")
            elif computer_total == user_total:
                print("It's a Drawww\n")
            else:
                print("You have won!!! Lesssgoooo!!!\n")

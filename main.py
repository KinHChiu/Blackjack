from tabnanny import check

import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game = True
computer = []
you = []
your_score = 0
computer_score = 0
play = "y"
hit = "y"
your_turn = 'y'
computer_turn = 'y'
def starting_hand():                            #Starting hand deal
    you.append(random.choice(cards))
    you.append(random.choice(cards))
    computer.append(random.choice(cards))
    computer.append(random.choice(cards))
def check_scores(cards):                            #Checks hand for total and removes 11 for 1s if over
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare_scores(yours, theirs):
    if yours> 21:
        print(f"You Lose! Your score: {yours} BUST!")
    elif theirs > 21:
        print(f"You Win! Computer Bust! Their score: {theirs}")
    elif yours > theirs and yours <= 21:
        print(f"You Win! Your score: {yours}   Theirs:  {theirs}")
    elif theirs > yours:
        print(f"You Lose! Your score: {yours}   Theirs:  {theirs}")
    elif theirs == yours:
        print(f"You Tied! Your score: {yours}   Theirs:  {theirs}")
    return(input("Do you want to play again? y or n").lower())

again = input("Do you want to play blackjack? y for yes n for no: ").lower()
while again == 'y':
    print(art.logo)
    your_turn = 'y'
    computer_turn = 'y'
    you = []
    computer = []
    starting_hand() #starting hand deal
    your_score = check_scores(you)
    computer_score = check_scores(computer)
    print(f"Your hand: {you}   Your total is: {your_score}")
    print(f"Computer's first card: {computer[0]}")
    if your_score == 0:
        print("You got BlackJack! you win!")
    else:
        while your_turn == 'y':
            hit = input("Do you want another card? Y or N?").lower()
            if hit == 'y':
                you.append(random.choice(cards))
                your_score = check_scores(you)
                print(f"Your hand: {you}   Your total is: {your_score}")
                if your_score == 0:
                    print("You got BlackJack! you win!")
                    your_turn = 'n'
                elif computer_score == 0:
                    print("Computer has BlackJack! you lose!")
                    your_turn = 'n'
                elif computer_score == 0 and your_score == 0:
                    print("You Both have Blackjack! You Tied!")
                    your_turn = 'n'
                elif your_score > 21:
                    your_turn = 'n'
            else:
                your_turn = 'n'
        while computer_turn == 'y':
            if your_score >= computer_score and computer_score < 17:
                computer.append(random.choice(cards))
                computer_score = check_scores(computer)
            else:
                computer_turn = 'n'
        again = compare_scores(your_score, computer_score)

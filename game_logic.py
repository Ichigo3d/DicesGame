import random

#
from player import Player

name1 = input("Input your name: ")
name2 = input("Input your name: ")

player1 = Player(name1)
player2 = Player(name2)


def throw_dices():
    dc_1 = generate_number()
    dc_2 = generate_number()
    return dc_1 + dc_2


def generate_number():
    return random.randint(1, 6)


def compare_scores(total_score1, total_score2):
    if total_score1 > total_score2:
        return 1
    elif total_score1 < total_score2:
        return 0
    elif total_score1 == total_score2:
        return -1


while True:
    print(f"{player1.name} it's your turn!")
    decision_player = input("input 'y' for throwing dices")
    if decision_player == "y":
        player1.total_score = throw_dices()
        print(player1.total_score)
    else:
        break

    print(f"{player2.name} it's your turn!")
    decision_player = input("input 'y' for throwing dices")
    if decision_player == "y":
        player2.total_score = throw_dices()
        print(player2.total_score)
    else:
        break

    result = compare_scores(player1.total_score, player2.total_score)

    if result == 1:
        print(f"{player1.name} is winner!")
        break
    elif result == 0:
        print(f"{player2.name} is winner!")
        break
    elif result == -1:
        print("Draw!!!")


dice1 = 0
dice2 = 0
total_score_player1 = 0
total_score_player2 = 0

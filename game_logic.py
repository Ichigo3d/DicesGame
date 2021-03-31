
from player import Player

name1 = input("Input your name: ")
name2 = input("Input your name: ")

player1 = Player(name1)
player2 = Player(name2)

player_list = [player1, player2]

def compare_scores(total_score1, total_score2):
    if total_score1 > total_score2:
        return 1
    elif total_score1 < total_score2:
        return 0
    elif total_score1 == total_score2:
        return -1


def sum_score(dc_1, dc_2):
    return dc_1 + dc_2


def select_winner(score1, score2):
    result = compare_scores(score1, score2)
    if result == 1:
        print("_______________________________")
        print(f"With a score of {score1}, player {player1.name} becomes the winner!")
        print("_______________________________")
    elif result == 0:
        print("_______________________________")
        print(f"With a score of {score2}, player {player2.name} becomes the winner!")
        print("_______________________________")
    elif result == -1:
        print("_______________________________")
        print("Draw!!!")
        print("_______________________________")

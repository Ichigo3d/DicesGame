
from dice import draw_dices, throw_dices
from player import Player

name1 = input("Input your name: ")
name2 = input("Input your name: ")

player1 = Player(name1)
player2 = Player(name2)

# player_list = [player1, player2]


def compare_scores(total_score1, total_score2):
    if total_score1 > total_score2:
        return 1
    elif total_score1 < total_score2:
        return 0
    elif total_score1 == total_score2:
        return -1


def sum_score(dc_1, dc_2):
    return dc_1 + dc_2


while True:
    print("_______________________________")
    print(f"{player1.name} it's your turn!")
    print("_______________________________")
    decision_player = input("input 'y' for throwing dices: ")
    print("_______________________________")
    if decision_player == "y":
        dc1, dc2 = throw_dices()
        player1.total_score = sum_score(dc1, dc2)
        draw_dices(dc1, dc2)
        print(f"Your total score is : {player1.total_score}!")
    else:
        print("Bye, see you soon!")
        break
    print("_______________________________")
    print(f"{player2.name} it's your turn!")
    print("_______________________________")
    decision_player = input("input 'y' for throwing dices: ")
    print("_______________________________")

    if decision_player == "y":
        dc1, dc2 = throw_dices()
        player2.total_score = sum_score(dc1, dc2)
        draw_dices(dc1, dc2)

        print(f"Your total score is : {player2.total_score}!")
    else:
        print("Bye, see you soon!")
        break

    result = compare_scores(player1.total_score, player2.total_score)

    if result == 1:
        print("_______________________________")
        print(f"With a score of {player1.total_score}, player {player1.name} becomes the winner!")
        print("_______________________________")
        decision_player = input("Do you want to play again? Input 'y':\n")
        if decision_player != "y":
            print("Bye, see you soon!")
            break
    elif result == 0:
        print("_______________________________")
        print(f"With a score of {player2.total_score}, player {player2.name} becomes the winner!")
        print("_______________________________")
        decision_player = input("Do you want to play again? Input 'y':\n")
        if decision_player != "y":
            print("Bye, see you soon!")
            break
    elif result == -1:
        print("Draw!!!")
        decision_player = input("Do you want to play again? Input 'y':\n")
        if decision_player != "y":
            print("Bye, see you soon!")
            break

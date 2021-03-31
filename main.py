from dice import throw_dices, draw_dices
from game_logic import *

break_flag = False

while True:
    for i in player_list:
        if not break_flag:
            print("_______________________________")
            print(f"{i.name} it's your turn!")
            print("_______________________________")
            decision_play = input("input 'y' for throwing dices: ")
            print("_______________________________")

            if decision_play == "y":
                dc1, dc2 = throw_dices()
                i.total_score = sum_score(dc1, dc2)
                draw_dices(dc1, dc2)
                print(f"Your total score is : {i.total_score}!")
            else:
                print("Bye, see you soon!")
                break_flag = True
                break

    if not break_flag:
        select_winner(player1.total_score, player2.total_score)
        decision_player = input("Do you want to play again? Input 'y':\n")
        if decision_player != "y":
            print("Bye, see you soon!")
            break
    else:
        break



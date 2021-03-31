class Dice:
    SIDE1 = ["_____________", "|           |", "|     *     |", "|           |", "|___________|"]
    SIDE2 = ["_____________", "|        *  |", "|           |", "|  *        |", "|___________|"]
    SIDE3 = ["_____________", "|        *  |", "|     *     |", "|  *        |", "|___________|"]
    SIDE4 = ["_____________", "|  *     *  |", "|           |", "|  *     *  |", "|___________|"]
    SIDE5 = ["_____________", "|  *     *  |", "|     *     |", "|  *     *  |", "|___________|"]
    SIDE6 = ["_____________", "|  *  *  *  |", "|           |", "|  *  *  *  |", "|___________|"]


def construct_sides(side1, side2):
    result = []
    for i in range(5):
        result.append(f"{side1[i]}    {side2[i]} ")
    return result



def draw_dices(side1, side2):
    num_side1 = connect_side(side1)
    num_side2 = connect_side(side2)
    constr = construct_sides(num_side1, num_side2)
    for i in constr:
        print(i)


def connect_side(number):
    if number == 1:
        return Dice.SIDE1
    elif number == 2:
        return Dice.SIDE2
    elif number == 3:
        return Dice.SIDE3
    elif number == 4:
        return Dice.SIDE4
    elif number == 5:
        return Dice.SIDE5
    elif number == 6:
        return Dice.SIDE6

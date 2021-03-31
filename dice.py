class Dice:
    SIDE1 = ["_____________", "|           |", "|     *     |", "|           |", "|___________|"]
    SIDE2 = ["_____________", "|        *  |", "|           |", "|  *        |", "|___________|"]
    SIDE3 = ["_____________", "|        *  |", "|     *     |", "|  *        |", "|___________|"]
    SIDE4 = ["_____________", "|  *     *  |", "|           |", "|  *     *  |", "|___________|"]
    SIDE5 = ["_____________", "|  *     *  |", "|     *     |", "|  *     *  |", "|___________|"]
    SIDE6 = ["_____________", "|  *  *  *  |", "|           |", "|  *  *  *  |", "|___________|"]


def draw_dice(side):
    num_side = connect_side(side)
    for i in num_side:
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

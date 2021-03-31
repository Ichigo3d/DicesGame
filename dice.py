import random


class Dice:
    SIDE1 = ["_____________", "|           |", "|     *     |", "|           |", "|___________|"]
    SIDE2 = ["_____________", "|        *  |", "|           |", "|  *        |", "|___________|"]
    SIDE3 = ["_____________", "|        *  |", "|     *     |", "|  *        |", "|___________|"]
    SIDE4 = ["_____________", "|  *     *  |", "|           |", "|  *     *  |", "|___________|"]
    SIDE5 = ["_____________", "|  *     *  |", "|     *     |", "|  *     *  |", "|___________|"]
    SIDE6 = ["_____________", "|  *  *  *  |", "|           |", "|  *  *  *  |", "|___________|"]


def construct_sides(side1, side2):
    """
    this func takes two arrays and combines them to 1
    param side1 is one of the constants aka SIDE1
    param side2 is the same as side1
    return array of combination of two sides
    """
    result = []
    for i in range(5):
        result.append(f"{side1[i]}    {side2[i]} ")
    return result


def draw_dices(side1, side2):
    """
    This func takes results of func throw_dices() and draws it in console
    param side1 integer
    param side2 integer
    return nothing, just print constr in console
    """
    num_side1 = connect_side(side1)
    num_side2 = connect_side(side2)
    construction = construct_sides(num_side1, num_side2)
    for i in construction:
        print(i)


def connect_side(number):
    """
    this func takes result of generate_number() and connect to the Dice's constant
    """
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


def throw_dices():
    """
    call func generate_number and return results
    """
    dc_1 = generate_number()
    dc_2 = generate_number()
    return dc_1, dc_2


def generate_number():
    """
    generate random integer and return it
    """
    return random.randint(1, 6)

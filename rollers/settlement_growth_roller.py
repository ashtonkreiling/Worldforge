import random

def grow_settlement():
    roll = random.randint(1, 6)
    return determine_growth(roll)


def determine_growth(roll):
    if roll == 1:
        return -1  # Settlement shrinks
    elif roll in [2, 3, 4]:
        return 0   # Settlement stays the same
    else:  # roll is 5 or 6
        return 1   # Settlement grows

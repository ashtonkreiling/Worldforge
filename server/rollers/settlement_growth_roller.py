import random

SETTLEMENT_GROWTH_VALUES = [-1, 0, 0, 0, 1, 1]

def grow_settlement():
    roll = random.randint(0, 5)
    return determine_growth(roll)


def determine_growth(roll):
    if 0 <= roll <= 5:
        return SETTLEMENT_GROWTH_VALUES[roll]
    else:
        raise ValueError(f"Roll must be between 0 and 5, got {roll}")

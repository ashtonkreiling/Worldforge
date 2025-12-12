import random


def roll_settlement_growth():
    """
    Rolls a d6 to determine settlement growth.
    
    Returns:
        int: -1 if settlement shrinks (rolled 1),
             0 if settlement stays the same (rolled 2-4),
             1 if settlement grows (rolled 5-6)
    """
    roll = random.randint(1, 6)
    
    if roll == 1:
        return -1  # Settlement shrinks
    elif roll in [2, 3, 4]:
        return 0   # Settlement stays the same
    else:  # roll is 5 or 6
        return 1   # Settlement grows


from abc import ABC, abstractmethod
import random


class Deity(ABC):
    
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power
    
    @abstractmethod
    def take_turn(self):
        pass
    
    def increment_power(self):
        """Roll 2d6 and increase power by the result."""
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        total = roll1 + roll2
        self.power += total


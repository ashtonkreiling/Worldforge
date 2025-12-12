from abc import ABC, abstractmethod


class Deity(ABC):
    
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power
    
    @abstractmethod
    def take_turn(self):
        pass


from abc import ABC, abstractmethod

class Action(ABC):

    def __init__(self, name: str, cost: int):
        self.name = name
        self.cost = cost

    @abstractmethod
    def take_action(self):
        pass

    def to_text(self):
        print(f"| {self.name:<30} | {self.cost:>2} |")

    def matches_name(self, user_input: str) -> bool:
        return self.name.lower() == user_input.lower()
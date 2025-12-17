from deities.deity import Deity
from actions.action import Action

class LesserDeity(Deity):
    def __init__(self, name: str, charge: str, power: int, actions: list[Action], questions: list[str]):
        self.charge = charge
        super().__init__(name, power, actions, questions)

    def to_text(self):
        print(f"Name: {self.name}")
        print(f"Charge: {self.charge}")
        print(self.description)
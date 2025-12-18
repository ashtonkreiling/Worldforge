from deities.deity import Deity
from actions.action import Action
from objects.object import Object

class LesserDeity(Deity):
    def __init__(self, name: str, charge: Object, power: int, actions: list[Action], questions: list[str]):
        self.charge = charge
        super().__init__(name, power, actions, questions)

    def to_text(self):
        print(f"Name: {self.name}")
        print("Charge ---------------------")
        self.charge.to_text()
        print("----------------------------")
        print(self.description)
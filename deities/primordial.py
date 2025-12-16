from deities.deity import Deity
from actions.primordial_actions import PrimordialAction
from actions.primordial_actions import PRIMORDIAL_ACTIONS

class Primordial(Deity):
    def __init__(self, name: str = "Primordial", power: int = 4, actions: list[PrimordialAction] = PRIMORDIAL_ACTIONS):
        questions = ["Q?"]
        super().__init__(name, power, actions, questions)

    def take_turn(self):
        self.increment_power()
        self.take_actions()

    
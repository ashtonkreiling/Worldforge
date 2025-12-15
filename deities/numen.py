from deities.deity import Deity
from actions.numen_actions import NumenAction
from actions.numen_actions import NUMEN_ACTIONS

class Numen(Deity):
    def __init__(self, name: str = "Sovereign", power: int = 4, actions: list[NumenAction] = NUMEN_ACTIONS):
        super().__init__(name, power, actions)

    def take_turn(self):
        self.increment_power()
        self.take_actions()
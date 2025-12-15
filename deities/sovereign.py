from deities.deity import Deity
from actions.sovereign_actions import SovereignAction
from actions.sovereign_actions import SOVEREIGN_ACTIONS

class Sovereign(Deity):
    def __init__(self, name: str = "Sovereign", power: int = 4, actions: list[SovereignAction] = SOVEREIGN_ACTIONS):
        super().__init__(name, power, actions)

    def take_turn(self):
        self.increment_power()
        self.take_actions()
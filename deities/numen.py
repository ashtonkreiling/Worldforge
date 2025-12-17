from deities.lesser_deity import LesserDeity
from actions.numen_actions import NumenAction
from actions.numen_actions import NUMEN_ACTIONS

class Numen(LesserDeity):
    def __init__(self, name: str = "Sovereign", charge: str = "", power: int = 4, actions: list[NumenAction] = NUMEN_ACTIONS):
        questions = [
            "How does this Numen appear to mortals when it chooses to be seen?",
            "What mood or personality does this Numen have?",
            "How does this Numen interact with its charge? Does it protect, test, punish, or bargain with them?",
            "What offerings or rituals please this Numen, what offends it?",
            "How does this Numen relate to other spirits nearby, or to the Patron or Sovereign above it?",
            "What symbols, charms, or tokens represent this Numen?"
        ]
        self.charge = charge
        super().__init__(name, charge, power, actions, questions)

    def take_turn(self):
        self.increment_power()
        self.take_actions()
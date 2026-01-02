from server.deities.lesser_deity import LesserDeity
from server.actions.action import Action
from server.actions.action_context import ActionContext
from server.actions.numen_actions import NUMEN_ACTIONS
from server.objects.faction import Faction

class Numen(LesserDeity):
    def __init__(self, name: str = "Numen", power: int = 4, actions: list[Action] = NUMEN_ACTIONS):
        questions = [
            "How does this Numen appear to mortals when it chooses to be seen?",
            "What mood or personality does this Numen have?",
            "How does this Numen interact with its charge? Does it protect, test, punish, or bargain with them?",
            "What offerings or rituals please this Numen, what offends it?",
            "How does this Numen relate to other spirits nearby, or to the Patron or Sovereign above it?",
            "What symbols, charms, or tokens represent this Numen?"
        ]
        charge = self.create_charge()
        super().__init__(name, charge, power, actions, questions)

    def create_charge(self):
        print("Creating the faction that is this numen's charge")
        return Faction()

    def take_turn(self):
        self.increment_power()
        self.take_actions()

    def set_context(self, action):
        return ActionContext(
            self,
            action.formatted_name,
            self.charge,
            1,
        )
from server.deities.deity import Deity
from server.actions.action import Action
from server.actions.primordial_actions import PRIMORDIAL_ACTIONS
from server.actions.action_context import ActionContext

class Primordial(Deity):
    def __init__(self, name: str = "Primordial", power: int = 0, actions: list[Action] = PRIMORDIAL_ACTIONS):
        questions = [
            "What is the appearance of this Primordial when viewed by an observer?",
            "When this Primordial moves, acts, or rests, how does the world react?",
            "What overarching goal or drives does this Primordial have?",
            "Is it possible for other entities (lesser deities, sentient species) to communicate with this Primordial? If so, how does the Primordial communicate?",
            "What symbols, color palette, or other visual markers represent them?"
        ]
        super().__init__(name, power, actions, questions)

    def take_turn(self):
        self.increment_power()
        self.take_actions()

    def set_context(self, action):
        return ActionContext(
            self,
            action.formatted_name,
            self.set_subject(action),
        )
    
    def set_subject(self, action: Action):
        # Primordials can take action on many different subjects so we need some handling logic eventually
        return None







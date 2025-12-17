from deities.deity import Deity
from actions.sovereign_actions import SovereignAction
from actions.sovereign_actions import SOVEREIGN_ACTIONS

class Sovereign(Deity):
    def __init__(self, name: str = "Sovereign", charge: str = "", power: int = 4, actions: list[SovereignAction] = SOVEREIGN_ACTIONS):
        questions = [
            "How does this Sovereign appear to their followers?",
            "What goals and machinations does this Sovereign have?",
            "What character attributes does this Sovereign have that are emulated by its followers?",
            "What symbols represent this Sovereign?",
            "If there are other Sovereigns in the setting, how does this Sovereign feel about them?",
            "How does this Sovereign feel about the Primordials in the setting?",
            "How has this Sovereign shaped the culture, morals, or laws of their species? What rituals or customs exist because of them?",
            "How directly does this Sovereign intervene in the lives of its followers? Rarely, through omens, through avatars, or through prophets?",
            "Is there tension between the species’ actual behavior and this Sovereign’s ideals? How is this tension handled?",
            "Are there relics, temples, or locations that are closely tied to this Sovereign’s essence or influence?",
            "If this Sovereign were a character in a story, how would you describe their temperament or role (mentor, judge, trickster, tyrant, guide, etc.)?"
        ]
        self.charge = charge
        super().__init__(name, power, actions, questions)

    def take_turn(self):
        self.increment_power()
        self.take_actions()
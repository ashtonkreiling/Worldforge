from actions.action import Action

class SovereignAction(Action):
    def take_action(self):
        return self.cost

SOVEREIGN_ACTIONS = [
    SovereignAction("Rest", 0),
    SovereignAction("Inspire New Settlement", 2),
    SovereignAction("Spark Enmity/Friendship", 3),
    SovereignAction("Bless Settlement", 4),
    SovereignAction("Create Hero", 10),
    SovereignAction("Save Charge from Cataclysm", 7),
    SovereignAction("Bind Other Sovereign", 8),
    SovereignAction("Aid in Battle", 3),
    SovereignAction("Gift Knowledge", 4),
    SovereignAction("Enact Taboo", 3),
    SovereignAction("Shape Culture", 4),
    SovereignAction("Shape Faith", 4),
    SovereignAction("Bestow Artifact", 5),
    SovereignAction("Curse", 8),
    SovereignAction("Immortalize Hero", 10),
]

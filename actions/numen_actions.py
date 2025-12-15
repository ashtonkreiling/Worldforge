from actions.action import Action

class NumenAction(Action):
    def take_action(self):
        return self.cost

NUMEN_ACTIONS = [
    NumenAction("Rest", 0),
    NumenAction("Bless", 4),
    NumenAction("Curse", 6),
    NumenAction("Enact Taboo", 3),
    NumenAction("Shape Faith", 3),
    NumenAction("Bestow Artifact", 10),
    NumenAction("Inspire Project", 10)
]

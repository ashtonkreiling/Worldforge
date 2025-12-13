from actions.action import Action

class PatronAction(Action):
    def take_action(self):
        return self.cost

PATRON_ACTIONS = [
    PatronAction("Rest", 0),
    PatronAction("Inspire Project", 6),
    PatronAction("Command War", 10),
    PatronAction("Aid in Battle", 6),
    PatronAction("Create Hero", 12),
    PatronAction("Shape Culture", 4),
    PatronAction("Shape Faith", 4),
    PatronAction("Enact Taboo", 3),
    PatronAction("Curse", 8),
    PatronAction("Bestow Artifact", 10)
]
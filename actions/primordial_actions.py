from actions.action import Action

class PrimordialAction(Action):
    def take_action(self):
        return self.cost

PRIMORDIAL_ACTIONS = [
    PrimordialAction("Rest", 0),
    PrimordialAction("Raise/Lower Land (9 Hexes)", 8),
    PrimordialAction("Shape Land (1 Hex)", 1),
    PrimordialAction("Add Resource", 1),
    PrimordialAction("Create Creature", 1),
    PrimordialAction("Create Leviathan", 10),
    PrimordialAction("Create Sentient Species", 10),
    PrimordialAction("Uplift Creature", 8),
    PrimordialAction("Create Subrace", 5),
    PrimordialAction("Catastrophe", 5),
    PrimordialAction("Bind Other Primordial", 8),
    PrimordialAction("Command Leviathan", 2)
]

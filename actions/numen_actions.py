from actions.action import Action
from actions.effects import AddHistory, AddChildObject

from objects.advantage import Advantage

NUMEN_ACTIONS = [
    Action("Rest", 0, []),
    Action("Bless", 4, [
        AddHistory,
        AddChildObject(Advantage())
    ]),
    Action("Curse", 6),
    Action("Enact Taboo", 3),
    Action("Shape Faith", 3),
    Action("Bestow Artifact", 10),
    Action("Inspire Project", 10)
]

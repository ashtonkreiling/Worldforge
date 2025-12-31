from actions.action import Action
from actions.effects import AddHistory, AddChildObject, AddBlessing, AddCurse

from objects.artifact import Artifact
from objects.project import Project

NUMEN_ACTIONS = [
    Action("Rest", 0, [], "rested"),
    Action("Bless", 4, [
        AddHistory(),
        AddBlessing(1),
    ], "blessed"),
    Action("Curse", 6, [
        AddHistory(),
        AddCurse(1),
    ], "cursed"),
    Action("Enact Taboo", 3, [AddHistory()], "enacted a taboo on"),
    Action("Shape Faith", 3, [AddHistory()], "shaped the faith of"),
    Action("Bestow Artifact", 10, [
        AddHistory(),
        AddChildObject(Artifact)
    ], "bestowed an artifact on"),
    Action("Inspire Project", 10, [
        AddHistory(),
        AddChildObject(Project)
    ], "inspired a project for")
]

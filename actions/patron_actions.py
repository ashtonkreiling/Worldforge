from actions.action import Action
from actions.effects import AddHistory, AddChildObject, AddBlessing, AddCurse, ResolveBattle, AidInBattle

from objects.artifact import Artifact
from objects.project import Project
from objects.hero import Hero

PATRON_ACTIONS = [
    Action("Rest", 0, [], "rested"),
    Action("Inspire Project", 6, [
        AddHistory(),
        AddChildObject(Project)
    ], "inspired a project for"),
    Action("Command Battle", 10, [
        AddHistory(),
        ResolveBattle()
    ], "commanded battle of"),
    Action("Aid in Battle", 6, [
        AddHistory(),
        AidInBattle(2)
    ], "in battle came to the aid of"),
    Action("Create Hero", 12, [
        AddHistory(),
        AddChildObject(Hero)
    ], "gave a hero to" ),
    Action("Shape Culture", 4, [AddHistory()], "shaped the culture of"),
    Action("Shape Faith", 4, [AddHistory()], "shaped the faith of"),
    Action("Enact Taboo", 3, [AddHistory()], "enacted a taboo on"),
    Action("Bless", 6, [
        AddHistory(),
        AddBlessing(2)
    ], "blessed"),
    Action("Curse", 8, [
        AddHistory(),
        AddCurse(2),
    ], "cursed"),
    Action("Bestow Artifact", 10, [
        AddHistory(),
        AddChildObject(Artifact)
    ], "bestowed an artifact on")
]
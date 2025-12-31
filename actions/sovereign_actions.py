from actions.action import Action

from actions.effects import CreateSettlement, AddHistory, CreateRelationship

SOVEREIGN_ACTIONS = [
    Action("Rest", 0),
    Action("Inspire New Settlement", 2, [
        AddHistory(),
        CreateSettlement()
    ], "inspired a new settlement of"),
    Action("Spark Enmity/Friendship", 3, [
        AddHistory(),
        CreateRelationship(),
    ], "changed the relationship of"),
    Action("Bless Settlement", 4),
    Action("Create Hero", 10),
    Action("Save Charge from Cataclysm", 7),
    Action("Bind Other Sovereign", 8),
    Action("Aid in Battle", 3),
    Action("Gift Knowledge", 4),
    Action("Enact Taboo", 3),
    Action("Shape Culture", 4),
    Action("Shape Faith", 4),
    Action("Bestow Artifact", 5),
    Action("Curse", 8),
    Action("Immortalize Hero", 10),
]

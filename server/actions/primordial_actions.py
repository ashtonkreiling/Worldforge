from server.actions.action import Action

PRIMORDIAL_ACTIONS = [
    Action("Rest", 0, [], "rested"),
    Action("Shape Land (1 Hex)", 1, [], "shaped land"),
    Action("Add Resource", 1, [], "added a resource"),
    Action("Create Creature", 1, [], "created a creature"),
    Action("Create Leviathan", 10, [], "created a leviathan"),
    Action("Create Sentient Species", 10, [], "created a sentient species"),
    Action("Uplift Creature", 9, [], "uplifted a creature"),
    Action("Create Subrace", 5, [], "created a subrace"),
    Action("Catastrophe", 5, [], "caused a catastrophe"),
    Action("Bind Other Primordial", 8, [], "bound a different primordial"),
    Action("Command Leviathan", 2, [], "commanded a leviathan")
]

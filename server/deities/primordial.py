from server.deities.deity import Deity
from server.actions.action import Action
from server.actions.action_context import ActionContext

from server.world.hex import Hex

from server.objects.resource import Resource
from server.objects.creature import Creature
from server.objects.leviathan import Leviathan

class Primordial(Deity):
    def __init__(self, name: str = "Primordial", power: int = 0):
        questions = [
            "What is the appearance of this Primordial when viewed by an observer?",
            "When this Primordial moves, acts, or rests, how does the world react?",
            "What overarching goal or drives does this Primordial have?",
            "Is it possible for other entities (lesser deities, sentient species) to communicate with this Primordial? If so, how does the Primordial communicate?",
            "What symbols, color palette, or other visual markers represent them?"
        ]
        super().__init__(name, power, questions)

    def take_turn(self):
        self.increment_power()
        self.take_actions()
    
    def set_actions(self):
        return [
            Action("Rest", 0),
            ShapeLand(self),
            AddResource(self),
            CreateCreature(self),
            CreateLeviathan(self),
            Action("Create Sentient Species", 10),
            Action("Uplift Creature", 9),
            Action("Create Subrace", 5),
            Action("Catastrophe", 5),
            Action("Bind Other Primordial", 8),
            Action("Command Leviathan", 2)
        ]
    
    def set_subject(self, action: Action):
        # Primordials can take action on many different subjects so we need some handling logic eventually
        return None


class PrimordialAction(Action):
    def __init__(self, name, cost, deity):
        self.deity = deity
        super().__init__(name, cost)

    def unpack_world_context(self, context):
        return [context["year"], context["world"]]

    def unpack_hex_context(self, context):
        return [context["q"], context["r"]]
    
    def unpack_extended_hex_context(self, context):
        return [context["height"], context["color"], context["terrain"]]
    
    def unpack_object_context(self, context):
        return [context["name"], context["description"], context["tags"]]

class ShapeLand(PrimordialAction):
    def __init__(self, deity):
        super().__init__("Shape Land", 1, deity)

    def take_action(self, context):
        # Context needs: q, r, height, color, terrain, year(round)
        year, world = self.unpack_world_context(context)
        q, r = self.unpack_hex_context(context)
        height, color, terrain = self.unpack_extended_hex_context(context)
        self.deity.description += f"\nDuring year {year} {self.deity.name} shaped the hex at {q},{r}"
        world.changed_hexes[(q,r)] = Hex(q, r, height, color, terrain)
        return self.cost
    
class AddResource(PrimordialAction):
    def __init__(self, deity):
        super().__init__("Add Resource", 1, deity)

    def take_action(self, context):
        # Context needs: q, r, name, description, tags, year(round)
        year, world = self.unpack_world_context(context)
        q, r = self.unpack_hex_context(context)
        name, description, tags = self.unpack_object_context(context)
        self.deity.description += f"\nDuring year {year} {self.name} added a resource to the hex at {q},{r}"

        hex = world.changed_hexes[(q,r)]
        if hex == None:
            hex = Hex(q, r, 0, (16,89,100), "")
            world.changed_hexes[(q,r)] = hex
        
        resource = Resource(name, description, tags)
        hex.resources.append(resource)

        return self.cost

class CreateCreature(PrimordialAction):
    def __init__(self, deity):
        super().__init__("Create Creature", 1, deity)

    def take_action(self, context):
        # Context needs: q, r, name, description, tags, year(round)
        year, world = self.unpack_world_context(context)
        q, r = self.unpack_hex_context(context)
        name, description, tags = self.unpack_object_context(context)
        self.deity.description += f"\nDuring year {year} {self.name} added a new creature to the hex at {q},{r}"

        hex = world.changed_hexes[(q,r)]
        if hex == None:
            hex = Hex(q, r, 0, (16,89,100), "")
            world.charged_hexes[(q,r)] = hex
        
        creature = Creature(name, description, tags)
        hex.creatures.append(creature)

        return self.cost
    
class CreateLeviathan(PrimordialAction):
    def __init__(self, deity):
        super().__init__("Create Leviathan", 10, deity)

    def take_action(self, context):
        # Context needs: q, r, name, description, tags, year(round)
        year, world = self.unpack_world_context(context)
        q, r = self.unpack_hex_context(context)
        name, description, tags = self.unpack_object_context(context)
        self.deity.description += f"\nDuring year {year} {self.name} added a new creature to the hex at {q},{r}"

        hex = world.changed_hexes[(q,r)]
        if hex == None:
            hex = Hex(q, r, 0, (16,89,100), "")
            world.charged_hexes[(q,r)] = hex
        
        leviathan = Leviathan(name, description, tags)
        hex.leviathans.append(leviathan)

        return self.cost


Action("Create Sentient Species", 10),
Action("Uplift Creature", 9),
Action("Create Subrace", 5),
Action("Catastrophe", 5),
Action("Bind Other Primordial", 8),
Action("Command Leviathan", 2)





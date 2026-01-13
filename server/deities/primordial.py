from server.deities.deity import Deity
from server.actions.action import Action
from server.actions.action_context import ActionContext

from server.world.hex import Hex

from server.objects.resource import Resource
from server.objects.creature import Creature
from server.objects.leviathan import Leviathan
from server.objects.cataclysm import Cataclysm

class Primordial(Deity):
    def __init__(self, name: str = "Primordial", power: int = 0):
        questions = [
            "What is the appearance of this Primordial when viewed by an observer?",
            "When this Primordial moves, acts, or rests, how does the world react?",
            "What overarching goal or drives does this Primordial have?",
            "Is it possible for other entities (lesser deities, sentient species) to communicate with this Primordial? If so, how does the Primordial communicate?",
            "What symbols, color palette, or other visual markers represent them?"
        ]
        self.child_sovereigns = []
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
            CreateSentient(self),
            UpliftCreature(self),
            CreateSubrace(self),
            CauseCataclysm(self),
            BindOtherPrimordial(self),
            CommandLeviathan(self)
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
        return [context["height_delta"], context["color"], context["terrain"]]
    
    def unpack_object_context(self, context):
        return [context["name"], context["description"], context["tags"]]
    
    def extended_hex_fields(self):
        return {
            "height_delta": {"type": "increment"},
            "terrain": {"type": "string"}
        }
    
    def object_fields(self):
        return {
            "name": {"type": "string"},
            "description": {"type": "string"},
            "tags": {"type": "tag", "options": ["test"]}
        }

class ShapeLand(PrimordialAction):
    def __init__(self, deity):
        super().__init__("Shape Land", 1, deity)

    def take_action(self, context):
        # Context needs: q, r, height, color, terrain, year(round)
        year, world = self.unpack_world_context(context)
        q, r = self.unpack_hex_context(context)
        height_delta, color, terrain = self.unpack_extended_hex_context(context)
        self.deity.description += f"\nDuring year {year} {self.deity.name} shaped the hex at {q},{r}"

        old_hex = world.changed_hexes.get((q, r))

        if old_hex is not None:
            height = old_hex.height + height_delta
        else:
            height = height_delta


        world.changed_hexes[(q,r)] = Hex(q, r, height, color, terrain)
        return self.cost
    
    def fields(self):
        return self.extended_hex_fields()
    
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
    
    def fields(self):
        return self.object_fields()

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
    
    def fields(self):
        return self.object_fields()
    
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

    def fields(self):
        return self.object_fields()
    
class CreateSentient(PrimordialAction):
    def __init__(self, deity):
        super().__init__("Create Sentient Species", 10, deity)

    def take_action(self, context):
        year, world = self.unpack_world_context(context)
        q, r = self.unpack_hex_context(context)
        sovereign_name = context["sovereign_name"]
        sovereign_appearance = context["sovereign_appearance"]
        sovereign_goals = context["sovereign_goals"]
        sovereign_attributes = context["sovereign_attributes"]
        sovereign_symbols = context["sovereign_symbols"]
        sovereign_relationships = context["sovereign_relationships"]
        sovereign_primordial_relationships = context["sovereign_primordial_relationships"]
        sovereign_rituals = context["sovereign_rituals"]
        sovereign_intervention = context["sovereign_intervention"]
        sovereign_tension = context["sovereign_tension"]
        sovereign_temples = context["sovereign_temples"]
        sovereign_characterization = context["sovereign_characterization"]
        first_settlement_name = context["first_settlement_name"]
        first_settlement_description = context["first_settlement_description"]
        first_settlement_tags = context["first_settlement_tags"]
        sentient_species_name = context["sentient_species_name"]
        sentient_species_description = context["sentient_species_description"]
        sentient_species_tags = context["sentient_species_tags"]

    def fields(self):
        return {
            "sovereign_name": {"type": "string"},
            "sovereign_appearance": {
                "type": "string",
                "ui_prompt": "How does this Sovereign appear to their followers?"
            },
            "sovereign_goals": {
                "type": "string",
                "ui_prompt": "What goals and machinations does this Sovereign have?"
            },
            "sovereign_attributes": {
                "type": "string",
                "ui_prompt": "What character attributes does this Sovereign have that are emulated by its followers?"
            },
            "sovereign_symbols": {
                "type": "string",
                "ui_prompt": "What symbols represent this Sovereign?"
            },
            "sovereign_relationships": {
                "type": "string",
                "ui_prompt": "If there are other Sovereigns in the setting, how does this Sovereign feel about them?"
            },
            "sovereign_primordial_relationships": {
                "type": "string",
                "ui_prompt": "How does this Sovereign feel about the Primordials in the setting?"
            },
            "sovereign_rituals": {
                "type": "string",
                "ui_prompt": "How has this Sovereign shaped the culture, morals, or laws of their species? What rituals or customs exist because of them?"
            },
            "sovereign_intervention": {
                "type": "string",
                "ui_prompt": "How directly does this Sovereign intervene in the lives of its followers? Rarely, through omens, through avatars, or through prophets?"
            },
            "sovereign_tension": {
                "type": "string",
                "ui_prompt": "Is there tension between the species’ actual behavior and this Sovereign’s ideals? How is this tension handled?",
            },
            "sovereign_temples": {
                "type": "string",
                "ui_prompt": "Are there relics, temples, or locations that are closely tied to this Sovereign’s essence or influence?"
            },
            "sovereign_characterization": {
                "type": "string",
                "ui_prompt": "If this Sovereign were a character in a story, how would you describe their temperament or role (mentor, judge, trickster, tyrant, guide, etc.)?"
            },
            "first_settlement_name": {"type": "string"},
            "first_settlement_description": {"type": "string"},
            "first_settlement_tags": {"type": "tag", "options": ["test"]},
            "sentient_species_name": {"type": "string"},
            "sentient_species_description": {"type": "string"},
            "sentient_species_tags": {"type": "tag", "options": ["test"]},
        }
    
class UpliftCreature(PrimordialAction):
    def __init__(self, deity):
        super().__init__("Uplift Creature", 9, deity)

    def take_action(self, context):
        year, world = self.unpack_world_context(context)
        q, r = self.unpack_hex_context(context)
        sovereign_name = context["sovereign_name"]
        sovereign_appearance = context["sovereign_appearance"]
        sovereign_goals = context["sovereign_goals"]
        sovereign_attributes = context["sovereign_attributes"]
        sovereign_symbols = context["sovereign_symbols"]
        sovereign_relationships = context["sovereign_relationships"]
        sovereign_primordial_relationships = context["sovereign_primordial_relationships"]
        sovereign_rituals = context["sovereign_rituals"]
        sovereign_intervention = context["sovereign_intervention"]
        sovereign_tension = context["sovereign_tension"]
        sovereign_temples = context["sovereign_temples"]
        sovereign_characterization = context["sovereign_characterization"]
        first_settlement_name = context["first_settlement_name"]
        first_settlement_description = context["first_settlement_description"]
        first_settlement_tags = context["first_settlement_tags"]
        sentient_species_name = context["sentient_species_name"]
        sentient_species_description = context["sentient_species_description"]
        sentient_species_tags = context["sentient_species_tags"]

    def fields(self):
        return {
            "sovereign_name": {"type": "string"},
            "sovereign_appearance": {
                "type": "string",
                "ui_prompt": "How does this Sovereign appear to their followers?"
            },
            "sovereign_goals": {
                "type": "string",
                "ui_prompt": "What goals and machinations does this Sovereign have?"
            },
            "sovereign_attributes": {
                "type": "string",
                "ui_prompt": "What character attributes does this Sovereign have that are emulated by its followers?"
            },
            "sovereign_symbols": {
                "type": "string",
                "ui_prompt": "What symbols represent this Sovereign?"
            },
            "sovereign_relationships": {
                "type": "string",
                "ui_prompt": "If there are other Sovereigns in the setting, how does this Sovereign feel about them?"
            },
            "sovereign_primordial_relationships": {
                "type": "string",
                "ui_prompt": "How does this Sovereign feel about the Primordials in the setting?"
            },
            "sovereign_rituals": {
                "type": "string",
                "ui_prompt": "How has this Sovereign shaped the culture, morals, or laws of their species? What rituals or customs exist because of them?"
            },
            "sovereign_intervention": {
                "type": "string",
                "ui_prompt": "How directly does this Sovereign intervene in the lives of its followers? Rarely, through omens, through avatars, or through prophets?"
            },
            "sovereign_tension": {
                "type": "string",
                "ui_prompt": "Is there tension between the species’ actual behavior and this Sovereign’s ideals? How is this tension handled?",
            },
            "sovereign_temples": {
                "type": "string",
                "ui_prompt": "Are there relics, temples, or locations that are closely tied to this Sovereign’s essence or influence?"
            },
            "sovereign_characterization": {
                "type": "string",
                "ui_prompt": "If this Sovereign were a character in a story, how would you describe their temperament or role (mentor, judge, trickster, tyrant, guide, etc.)?"
            },
            "first_settlement_name": {"type": "string"},
            "first_settlement_description": {"type": "string"},
            "first_settlement_tags": {"type": "tag", "options": ["test"]},
            "sentient_species_name": {"type": "string"},
            "sentient_species_description": {"type": "string"},
            "sentient_species_tags": {"type": "tag", "options": ["test"]},
        }
    
class CreateSubrace(PrimordialAction):
    def __init__(self, deity):
        super().__init__("Create Subrace", 5, deity)

    def take_action(self, context):
        year, world = self.unpack_world_context(context)
        q, r = self.unpack_hex_context(context)
        sovereign_name = context["sovereign_name"]
        sovereign_appearance = context["sovereign_appearance"]
        sovereign_goals = context["sovereign_goals"]
        sovereign_attributes = context["sovereign_attributes"]
        sovereign_symbols = context["sovereign_symbols"]
        sovereign_relationships = context["sovereign_relationships"]
        sovereign_primordial_relationships = context["sovereign_primordial_relationships"]
        sovereign_rituals = context["sovereign_rituals"]
        sovereign_intervention = context["sovereign_intervention"]
        sovereign_tension = context["sovereign_tension"]
        sovereign_temples = context["sovereign_temples"]
        sovereign_characterization = context["sovereign_characterization"]
        first_settlement_name = context["first_settlement_name"]
        first_settlement_description = context["first_settlement_description"]
        first_settlement_tags = context["first_settlement_tags"]
        sentient_species_name = context["sentient_species_name"]
        sentient_species_description = context["sentient_species_description"]
        sentient_species_tags = context["sentient_species_tags"]

    def fields(self):
        return {
            "sovereign_name": {"type": "string"},
            "sovereign_appearance": {
                "type": "string",
                "ui_prompt": "How does this Sovereign appear to their followers?"
            },
            "sovereign_goals": {
                "type": "string",
                "ui_prompt": "What goals and machinations does this Sovereign have?"
            },
            "sovereign_attributes": {
                "type": "string",
                "ui_prompt": "What character attributes does this Sovereign have that are emulated by its followers?"
            },
            "sovereign_symbols": {
                "type": "string",
                "ui_prompt": "What symbols represent this Sovereign?"
            },
            "sovereign_relationships": {
                "type": "string",
                "ui_prompt": "If there are other Sovereigns in the setting, how does this Sovereign feel about them?"
            },
            "sovereign_primordial_relationships": {
                "type": "string",
                "ui_prompt": "How does this Sovereign feel about the Primordials in the setting?"
            },
            "sovereign_rituals": {
                "type": "string",
                "ui_prompt": "How has this Sovereign shaped the culture, morals, or laws of their species? What rituals or customs exist because of them?"
            },
            "sovereign_intervention": {
                "type": "string",
                "ui_prompt": "How directly does this Sovereign intervene in the lives of its followers? Rarely, through omens, through avatars, or through prophets?"
            },
            "sovereign_tension": {
                "type": "string",
                "ui_prompt": "Is there tension between the species’ actual behavior and this Sovereign’s ideals? How is this tension handled?",
            },
            "sovereign_temples": {
                "type": "string",
                "ui_prompt": "Are there relics, temples, or locations that are closely tied to this Sovereign’s essence or influence?"
            },
            "sovereign_characterization": {
                "type": "string",
                "ui_prompt": "If this Sovereign were a character in a story, how would you describe their temperament or role (mentor, judge, trickster, tyrant, guide, etc.)?"
            },
            "first_settlement_name": {"type": "string"},
            "first_settlement_description": {"type": "string"},
            "first_settlement_tags": {"type": "tag", "options": ["test"]},
            "sentient_species_name": {"type": "string"},
            "sentient_species_description": {"type": "string"},
            "sentient_species_tags": {"type": "tag", "options": ["test"]},
        }
    
class CauseCataclysm(PrimordialAction):
    def __init__(self, deity):
        super().__init__("Cause Cataclysm", 5, deity)

    def take_action(self, context):
        # Context needs: q, r, name, description, tags, year(round)
        year, world = self.unpack_world_context(context)
        q, r = self.unpack_hex_context(context)
        name, description, tags = self.unpack_object_context(context)
        self.deity.description += f"\nDuring year {year} {self.name} caused a catastrophe in the hex at {q},{r}"

        hex = world.changed_hexes[(q,r)]
        if hex == None:
            hex = Hex(q, r, 0, (16,89,100), "")
            world.charged_hexes[(q,r)] = hex
        
        cataclysm = Cataclysm(name, description, tags)
        hex.cataclysms.append(cataclysm)

        # Artifacts need to be moved from settlements to
        # parent hex at end of turn
        world.hexes_to_update[(hex.q,hex.r)] = hex
        hex.creatures = []

        return self.cost

    def fields(self):
        return self.object_fields()
    
class BindOtherPrimordial(PrimordialAction):
    def __init__(self, deity):
        super().__init__("Bind Other Primordial", 8, deity)

    def take_action(self, context):
        year, world = self.unpack_world_context(context)
        other_primordial_id = context["other_primordial"]
        other_deity = world.deities[other_primordial_id]
        other_deity.decrement_power()
        self.deity.description += f"\nDuring year {year} {self.name} bound {other_deity.name}"

    def fields(self):
        return {
            "other_primordial_id": {"type": "int"},
        }
    
class CommandLeviathan(PrimordialAction):
    def __init__(self, deity):
        super().__init__("Command Leviathan", 2, deity)

    def take_action(self, context):
        year, world = self.unpack_world_context(context)
        leviathan_id = context["leviathan_id"] # temporary
        leviathan_action = context["leviathan_action"]

    def fields(self):
        return {
            "leviathan_id": {"type": "int"},
            "leviathan_action": {"type": "tag", "options": ["attack", "move"]}
        }

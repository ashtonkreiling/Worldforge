import random

from server.actions.effect import Effect

from server.objects.object import Object
from server.objects.advantage import Advantage
from server.objects.disadvantage import Disadvantage
from server.objects.relationship import Relationship
from server.objects.sentient import Sentient
from server.deities.patron import Patron
from server.utils.prompt_player import prompt_player

class AddHistory(Effect):
    def apply(self, context, _world):
        context.subject.add_history_entry(context)

class EditHex(Effect):
    def apply(self, context, world):
        world.create_or_edit_hex(context.q, context.r, )

class AddBlessing(Effect):
    def __init__(self, magnitude: int):
        self.magnitude = magnitude
        super().__init__()

    def apply(self, context, _world):
        obj = Advantage(self.magnitude)
        obj.attach_to(context.subject)

class AidInBattle(Effect):
    def __init__(self, magnitude: int):
        self.magnitude = magnitude
        super().__init__()

    def apply(self, context, _world):
        obj = Advantage(self.magnitude, True)
        obj.attach_to(context.subject)

class AddCurse(Effect):
    def __init__(self, magnitude: int):
        self.magnitude = magnitude
        super().__init__()

    def apply(self, context, _world):
        obj = Disadvantage(self.magnitude)
        obj.attach_to(context.subject)

class AddChildObject(Effect):
    def __init__(self, object_klass: type[Object]):
        self.object_klass = object_klass

    def apply(self, context, _world):
        obj = self.object_klass()
        obj.attach_to(context.subject)

class CreateSettlement(Effect):
    def apply(self, context, _world):
        name = prompt_player("What is the name of the Patron of this new settlement?")
        return Patron(name, context.subject)
    
class CreateRelationship(Effect):
    def apply(self, context, _world):
        other = Sentient()
        description = prompt_player("What is the nature of the relationship?")
        return Relationship(description, context.subject, other)

class ResolveBattle(Effect):
    # This won't really work until we have a global map object but the skeleton is here
    def apply(self, context, _world):
        attacker = context.subject
        defender = prompt_player("Who are you attacking?")
        attacker_roll = self.roll_2d6() + self.apply_settlement_advantages(attacker)
        defender_roll = self.roll_2d6() + self.apply_settlement_advantages(defender)
        result = self.determine_result(attacker_roll, defender_roll)
    
    def apply_settlement_advantages(self, settlement):
        total = settlement.size
        for advantage in settlement.advantages:
            for tag in advantage.affected_tags:
                if tag == "battle":
                    total += 1

    def roll_2d6(self):
        return random.randint(1,6) + random.randint(1,6)
    
    # Still need to add the victory/loss table and consequences
    def determine_result(self, attacker_roll, defender_roll):
        difference = attacker_roll - defender_roll
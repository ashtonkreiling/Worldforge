import random

from actions.effect import Effect

from objects.object import Object
from objects.advantage import Advantage
from objects.disadvantage import Disadvantage

class AddHistory(Effect):
    def apply(self, context):
        context.subject.add_history_entry(context)

class AddBlessing(Effect):
    def apply(self, context):
        obj = Advantage(1)
        obj.attach_to(context.subject)

class AddCurse(Effect):
    def apply(self, context):
        obj = Disadvantage(-1)
        obj.attach_to(context.subject)

class AddChildObject(Effect):
    def __init__(self, object_klass: type[Object]):
        self.object_klass = object_klass

    def apply(self, context):
        obj = self.object_klass()
        obj.attach_to(context.subject)

class ResolveBattle(Effect):
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def apply(self, context):
        attacker_roll = self.roll_2d6() + self.apply_settlement_advantages(self.attacker)
        defender_roll = self.roll_2d6() + self.apply_settlement_advantages(self.defender)
        result = self.determine_result(attacker_roll, defender_roll)
        return super().apply(context)
    
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
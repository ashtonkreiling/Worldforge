from deities.deity import Deity
from objects.object import Object
from actions.action_context import ActionContext
from utils.prompt_player import prompt_player

class Event:
    def __init__(self, context: ActionContext):
        self.actor = context.actor
        self.action = context.action
        self.subject = context.subject
        self.turn = context.turn
        self.description = prompt_player(f"On turn {self.turn} the {type(self.actor).__name__} {self.actor.name} {self.action} {self.subject} to?")

    def to_text(self):
        return self.description
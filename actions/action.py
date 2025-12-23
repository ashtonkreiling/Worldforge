from actions.effect import Effect
from actions.action_context import ActionContext

class Action:

    def __init__(self, name: str, cost: int, effects: list[Effect], formatted_name: str):
        self.name = name
        self.cost = cost
        self.effects = effects
        self.formatted_name = formatted_name

    def take_action(self, context: ActionContext):
        for effect in self.effects:
            effect.apply(context)
        return self.cost

    def to_text(self):
        print(f"| {self.name:<30} | {self.cost:>2} |")

    def matches_name(self, user_input: str) -> bool:
        return self.name.lower() == user_input.lower()
class Action:

    def __init__(self, name: str, cost: int):
        self.name = name
        self.cost = cost

    def take_action(self):
        return self.cost

    def to_text(self):
        print(f"| {self.name:<30} | {self.cost:>2} |")

    def matches_name(self, user_input: str) -> bool:
        return self.name.lower() == user_input.lower()
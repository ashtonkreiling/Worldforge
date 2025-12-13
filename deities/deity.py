from abc import ABC, abstractmethod
from actions.action import Action
import random



class Deity(ABC):
    
    def __init__(self, name: str, power: int, actions: list[Action]):
        self.name = name
        self.power = power
        self.actions = actions
    
    @abstractmethod
    def take_turn(self):
        pass
    
    def increment_power(self):
        if self.power < 4:
            self.power += 4
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        total = roll1 + roll2
        self.power += total

    def take_actions(self):
        while self.power > 0:
            self.power_header_to_text()
            self.loop_actions_to_text()
            self.print_actions_table_footer()

            user_input = input()

            selected_action = self.get_selected_action(user_input)

            if selected_action.name == "Rest":
                return

            if selected_action:
                cost = selected_action.take_action()
                if cost <= self.power:
                    self.power -= cost
                else:
                    print("That action is too expensive for the power you have left")

    def power_header_to_text(self):
        print("---------------------------------------")
        print(f"| Current Power: {self.power:>20} |")
        print("---------------------------------------")

    def loop_actions_to_text(self):
        for action in self.actions:
            action.to_text()

    def print_actions_table_footer(self):
        print("---------------------------------------")
        print("Select an action from the list")

    def get_selected_action(self, user_input: str):
        if user_input.isdigit():
            index = int(user_input)
            if 0 <= index < len(self.actions):
                return self.actions[index]

        for action in self.actions:
            if action.matches_name(user_input):
                return action

        return None

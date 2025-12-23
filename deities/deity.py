import random
from abc import ABC, abstractmethod

from actions.action import Action
from actions.action_context import ActionContext

from utils.name_to_filename import to_filename
from utils.prompt_player import prompt_player



class Deity(ABC):
    
    def __init__(self, name: str, power: int, actions: list[Action], questions: list[str]):
        self.name = name
        self.power = power
        self.description = self.generate_description(questions)
        self.actions = actions
        self.file_path = to_filename(name)

    def generate_description(self, questions):
        description = ""
        for question in questions:
            answer = prompt_player(question)
            description += f"{question}\n{answer}\n"
        return description
    
    @abstractmethod
    def take_turn(self):
        pass

    def to_text(self):
        print(f"Name: {self.name}")
        print(self.description)
    
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
                cost = selected_action.cost
                if cost <= self.power:
                    context = ActionContext(
                        self,
                        selected_action.formatted_name,
                        self.charge,
                        1
                    )
                    self.power -= selected_action.take_action(context)
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

import random
from abc import ABC, abstractmethod

from server.actions.action import Action
from server.actions.action_context import ActionContext

from server.utils.name_to_filename import to_filename
from server.utils.prompt_player import prompt_player



class Deity(ABC):
    
    def __init__(self, name: str, power: int, questions: list[str]):
        self.name = name
        self.power = power
        self.description = "" # self.generate_description(questions)
        self.actions = self.set_actions()
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

    @abstractmethod
    def set_actions(self):
        pass

    def to_text(self):
        print(f"Name: {self.name}")
        print(self.description)

    def decrement_power(self):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        total = roll1 + roll2
        self.power -= total
    
    def increment_power(self):
        if self.power < 4:
            self.power += 4
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        total = roll1 + roll2
        self.power += total

    def take_action(self, index: int, context):
        if index == 0:
            print("Rested")
            return True # Flag to end turn
        if 0 <= index < len(self.actions):
            action =  self.actions[index]
            cost = action.cost
            if cost <= self.power:
                self.power -= action.take_action(context)
            else:
                print("That action is too expensive for the power you have left")
            return self.power <= 0
        return False

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
                    context = self.set_context(selected_action)
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

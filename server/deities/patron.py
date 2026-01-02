from server.rollers.settlement_growth_roller import grow_settlement
from server.rollers.cultural_question_roller import ask_cultural_question
from server.rollers.religion_question_roller import ask_religion_question
from server.rollers.random_events_roller import roll_random_event
from server.deities.lesser_deity import LesserDeity
from server.actions.action import Action
from server.actions.patron_actions import PATRON_ACTIONS
from server.objects.settlement import Settlement
from server.objects.sentient import Sentient
from server.utils.prompt_player import prompt_player

import random

class Patron(LesserDeity):    
    def __init__(self, name: str, species: Sentient, power: int = 4, actions: list[Action] = PATRON_ACTIONS):
        questions = [
            "How does this Patron appear when communicating with mortals?",
            "What goals does this Patron have?",
            "What character strengths and weaknesses does this Patron have?",
            "What symbols represent this Patron?",
            "Does this Patron live up to the ideal of its species' Sovereign?",
            "How does this Patron feel about its species' Sovereign?",
            "What relationship does this Patron have with other Patrons in the surrounding area?",
            "Are there holy sites dedicated to this Patron? What are they like?",
        ]
        charge = self.create_charge(species)
        super().__init__(name, charge, power, actions, questions)
    
    def create_charge(self, species):
        print("Creating the settlement that is this patron's charge")
        inhabitants = {species.name: random.randint(40, 80)}
        return Settlement(inhabitants)


    def take_turn(self):
        self.handle_settlement_growth()
        self.handle_cultural_question()
        self.handle_religion_question()
        self.handle_random_event()
        self.increment_power()
        self.take_actions()
    
    def handle_settlement_growth(self):
        result = grow_settlement()
        
        if result == -1:
            status = "shrunk"
        elif result == 0:
            status = "stayed the same"
        else:  # result == 1
            status = "grew"
        
        print(f"Settlement {status}")
    
    def handle_cultural_question(self):
        question = ask_cultural_question()
        prompt_player(question)
    
    def handle_religion_question(self):
        question = ask_religion_question()
        prompt_player(question)
    
    def handle_random_event(self):
        event = roll_random_event()
        print(event)
from rollers.settlement_growth_roller import grow_settlement
from rollers.cultural_question_roller import ask_cultural_question
from rollers.religion_question_roller import ask_religion_question
from rollers.random_events_roller import roll_random_event
from deities.lesser_deity import LesserDeity
from actions.patron_actions import PatronAction
from actions.patron_actions import PATRON_ACTIONS


class Patron(LesserDeity):    
    def __init__(self, name: str = "Patron", charge: str = "", power: int = 4, actions: list[PatronAction] = PATRON_ACTIONS):
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
        self.charge = charge
        super().__init__(name, charge, power, actions, questions)
    
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
        print(question)
        input()  # Wait for user response
    
    def handle_religion_question(self):
        question = ask_religion_question()
        print(question)
        input()  # Wait for user response
    
    def handle_random_event(self):
        event = roll_random_event()
        print(event)
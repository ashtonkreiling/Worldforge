from rollers.settlement_growth_roller import grow_settlement
from rollers.cultural_question_roller import ask_cultural_question
from rollers.religion_question_roller import ask_religion_question
from rollers.random_events_roller import roll_random_event


class Patron:    
    def __init__(self):
        pass
    
    def take_turn(self):
        self.handle_settlement_growth()
        self.handle_cultural_question()
        self.handle_religion_question()
        self.handle_random_event()
    
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

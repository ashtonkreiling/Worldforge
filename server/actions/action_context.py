class ActionContext:
    def __init__(self, actor, action, subject, turn = 0, q = 0, r = 0):
        self.actor = actor
        self.action = action
        self.subject = subject
        self.turn = turn
        self.q = q
        self.r = r

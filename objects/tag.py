class Tag:
    def __init__(self, type: str):
        self.type = type

    def to_text(self):
        print(f"Tag: {self.type}")
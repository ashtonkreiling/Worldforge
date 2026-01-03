from server.world.hex import Hex
from server.deities.primordial import Primordial

class WorldState:
    def __init__(self):
        self.deities = [Primordial(), Primordial("Primordial 2")]
        self.current_turn = 0 # Which Deity in self.deities is taking a turn
        self.current_round = 0 # What "year" of history it is right now
        self.changed_hexes = {
           (1,1): Hex(1,1,1,(100,89,16),"plains")
        }  # (q,r) -> Hex
        self.deities[0].increment_power()

    def format_hex_to_dict(self, hex: Hex):
        return {
            "q": hex.q,
            "r": hex.r,
            "height": hex.height,
            "color": hex.color,
        }

    def get_hex(self, q, r):
        hex = self.changed_hexes.get((q, r))
        if hex is None:
            return None
        return self.format_hex_to_dict(hex)


    def get_hexes_in_range(self, q_min, q_max, r_min, r_max):
        return [
            self.format_hex_to_dict(h) for (q,r), h in self.changed_hexes.items()
            if q_min <= q <= q_max and r_min <= r <= r_max
        ]

    def get_current_deity(self):
        return self.deities[self.current_turn]

    def get_turn_payload(self):
        deity = self.get_current_deity()
        return {
            "id": self.current_turn,
            "name": deity.name,
            "power": deity.power,
            "actions": [
                {
                    "index": i,
                    "name": action.name,
                    "cost": action.cost
                }
                for i, action in enumerate(deity.actions)
            ]
        }

    def apply_action(self, deity_id, action_index, q, r):
        deity = self.get_current_deity()

        if deity_id != self.current_turn:
            raise ValueError("Not your turn")
        
        end_turn = deity.take_action(action_index)

        if end_turn:
            self.increment_turn_or_round()
            self.get_current_deity().increment_power()


    def end_turn_if_needed(self):
        deity = self.get_current_deity()
        if deity.power <= 0:
            self.increment_turn_or_round()
            deity = self.get_current_deity()
            deity.increment_power()

    def increment_turn_or_round(self):
        if self.current_turn + 1 >= len(self.deities):
            self.current_round += 1
            self.current_turn = 0
        else:
            self.current_turn += 1
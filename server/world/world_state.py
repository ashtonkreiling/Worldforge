from server.world.hex import Hex

class WorldState:
    def __init__(self):
        self.changed_hexes = {
           (1,1): Hex(1,1,1,(100,89,16),"plains")
        }  # (q,r) -> Hex

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

    def apply_action(self, action):
        pass
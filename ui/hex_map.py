# ui/hex_map.py
import math
import pygame
from ui.hex import Hex

class HexMap:
    def __init__(self, radius, hex_size, center):
        self.radius = radius
        self.hex_size = hex_size
        self.center = center
        self.camera_offset = [0, 0]
        self.selected_hex = None

    def draw(self, surface):
        screen = surface.get_rect()
        ox, oy = self.camera_offset
        size = self.hex_size

        def pixel_to_axial(px, py):
            x = (px - ox - self.center[0]) / size
            y = (py - oy - self.center[1]) / size
            q = math.sqrt(3)/3 * x - 1/3 * y
            r = 2/3 * y
            return q, r

        q1, r1 = pixel_to_axial(screen.left, screen.top)
        q2, r2 = pixel_to_axial(screen.right, screen.bottom)

        q_min = math.floor(min(q1, q2)) - 6
        q_max = math.ceil(max(q1, q2)) + 6
        r_min = math.floor(min(r1, r2)) - 2
        r_max = math.ceil(max(r1, r2)) + 2

        for q in range(q_min, q_max + 1):
            for r in range(r_min, r_max + 1):
                if abs(q) > self.radius or abs(r) > self.radius or abs(q+r) > self.radius:
                    continue

                selected = self.selected_hex == (q, r)

                Hex.draw(
                    surface,
                    q, r,
                    size,
                    self.center,
                    offset=self.camera_offset,
                    selected=selected
                )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for q in range(-self.radius, self.radius + 1):
                for r in range(-self.radius, self.radius + 1):
                    if abs(q + r) > self.radius:
                        continue
                    if Hex.contains_point(
                        event.pos,
                        q, r,
                        self.hex_size,
                        self.center,
                        self.camera_offset
                    ):
                        self.selected_hex = (q, r)
                        return

    def pan(self, dx, dy):
        self.camera_offset[0] += dx
        self.camera_offset[1] += dy


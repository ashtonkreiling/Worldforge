import pygame

from ui.hex import Hex

class HexMap:
    def __init__(self, radius, hex_size, center):
        self.hexes = []
        self.center = center
        self.camera_offset = [0, 0]  # x, y

        for q in range(-radius, radius + 1):
            for r in range(-radius, radius + 1):
                if abs(q + r) <= radius:
                    self.hexes.append(Hex(q, r, hex_size, center))

    def draw(self, surface):
        for hex in self.hexes:
            hex.draw(surface, offset=self.camera_offset)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for hex in self.hexes:
                hex.selected = False
            for hex in self.hexes:
                if hex.contains_point(event.pos):
                    hex.selected = True
                    break

    def pan(self, dx, dy):
        """Move camera by dx, dy"""
        self.camera_offset[0] += dx
        self.camera_offset[1] += dy


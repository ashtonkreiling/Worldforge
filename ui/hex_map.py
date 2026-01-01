import pygame
import math

from ui.hex import Hex

class HexMap:
    def __init__(self, radius, hex_size, center):
        self.hexes = []
        self.center = center
        self.hex_size = hex_size
        self.radius = radius
        self.camera_offset = [0, 0]  # x, y

        for q in range(-radius, radius + 1):
            for r in range(-radius, radius + 1):
                if abs(q + r) <= radius:
                    self.hexes.append(Hex(q, r, hex_size, center))

    def draw(self, surface):
        screen_rect = surface.get_rect()
        offset_x, offset_y = self.camera_offset
        hex_size = self.hex_size

        # Convert pixel coords of screen corners to axial coordinates
        def pixel_to_axial(px, py):
            x = (px - offset_x - self.center[0]) / hex_size
            y = (py - offset_y - self.center[1]) / hex_size

            q = math.sqrt(3)/3 * x - 1/3 * y
            r = 2/3 * y
            return q, r

        # Top-left corner
        q_min_f, r_min_f = pixel_to_axial(screen_rect.left, screen_rect.top)
        # Bottom-right corner
        q_max_f, r_max_f = pixel_to_axial(screen_rect.right, screen_rect.bottom)

        # Add a margin of 1 hex to avoid clipping
        q_min = math.floor(q_min_f) - 6
        q_max = math.ceil(q_max_f) + 6
        r_min = math.floor(r_min_f) - 1
        r_max = math.ceil(r_max_f) + 1

        # Draw only hexes within axial bounding box
        for hex in self.hexes:
            if q_min <= hex.q <= q_max and r_min <= hex.r <= r_max:
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


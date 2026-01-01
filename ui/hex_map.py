import pygame
import math

from ui.hex import Hex

class HexMap:
    def __init__(self, radius, hex_size, center):
        self.hexes = []
        self.center = center
        self.hex_size = hex_size
        self.camera_offset = [0, 0]  # x, y

        for q in range(-radius, radius + 1):
            for r in range(-radius, radius + 1):
                if abs(q + r) <= radius:
                    self.hexes.append(Hex(q, r, hex_size, center))

    def draw(self, surface):
        screen_rect = surface.get_rect()
        offset_x, offset_y = self.camera_offset
        hex_size = self.hex_size

        # Compute approx max number of hexes that fit horizontally and vertically
        hex_width = math.sqrt(3) * hex_size
        hex_height = 2 * hex_size
        horiz_radius = int(screen_rect.width / hex_width) + 2
        vert_radius = int(screen_rect.height / (hex_height * 3/4)) + 2

        # Compute camera center in axial coordinates
        cam_q = round((screen_rect.centerx - offset_x) / (hex_size * math.sqrt(3)))
        cam_r = round((screen_rect.centery - offset_y) / (hex_size * 3/2))

        # Only draw hexes within this axial range
        for hex in self.hexes:
            if (
                cam_q - horiz_radius - 10 <= hex.q <= cam_q + horiz_radius and
                cam_r - vert_radius <= hex.r <= cam_r + vert_radius
            ):
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


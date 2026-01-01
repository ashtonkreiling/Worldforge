import math
import pygame

class Hex:
    def __init__(self, q, r, size, center):
        self.q = q
        self.r = r
        self.size = size
        self.center = center
        self.selected = False

    def pixel_center(self):
        x = self.size * (3/2 * self.q)
        y = self.size * (math.sqrt(3) * (self.r + self.q / 2))
        return (
            self.center[0] + x,
            self.center[1] + y
        )

    def corners(self):
        cx, cy = self.pixel_center()
        points = []
        for i in range(6):
            angle = math.pi / 3 * i
            px = cx + self.size * math.cos(angle)
            py = cy + self.size * math.sin(angle)
            points.append((px, py))
        return points

    def draw(self, surface):
        color = (100, 180, 255) if self.selected else (80, 80, 100)
        pygame.draw.polygon(surface, color, self.corners(), 0)
        pygame.draw.polygon(surface, (30, 30, 40), self.corners(), 2)
    
    def contains_point(self, point):
        polygon = self.corners()
        x, y = point
        inside = False

        n = len(polygon)
        px1, py1 = polygon[0]

        for i in range(n + 1):
            px2, py2 = polygon[i % n]

            if min(py1, py2) < y <= max(py1, py2):
                if x <= max(px1, px2):
                    if py1 != py2:
                        xinters = (y - py1) * (px2 - px1) / (py2 - py1) + px1
                    if px1 == px2 or x <= xinters:
                        inside = not inside

            px1, py1 = px2, py2

        return inside


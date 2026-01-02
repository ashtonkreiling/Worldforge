import pygame
import pygame_gui

from client.hex_map import HexMap
from client.hex import Hex

PAN_SPEED = 20

pygame.init()
Hex.font = pygame.font.SysFont("arial", 14)

WINDOW_SIZE = (1000, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("WorldForge")

clock = pygame.time.Clock()
manager = pygame_gui.UIManager(WINDOW_SIZE)

hex_map = HexMap(radius=100, hex_size=40, center=(500, 400))

running = True
while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        hex_map.handle_event(event)
        manager.process_events(event)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hex_map.pan(PAN_SPEED, 0)
    if keys[pygame.K_RIGHT]:
        hex_map.pan(-PAN_SPEED, 0)
    if keys[pygame.K_UP]:
        hex_map.pan(0, PAN_SPEED)
    if keys[pygame.K_DOWN]:
        hex_map.pan(0, -PAN_SPEED)

    manager.update(time_delta)

    screen.fill((20, 20, 25))
    hex_map.draw(screen)
    manager.draw_ui(screen)

    pygame.display.flip()

pygame.quit()

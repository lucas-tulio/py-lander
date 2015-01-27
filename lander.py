import pygame

class Lander:

  def __init__(self, surface):
    self.surface = surface
    self.x = 10.0
    self.y = 10.0

  def on_render(self):
    pygame.draw.polygon(self.surface, (255, 255, 255), ((self.x, self.y), (self.x + 10, self.y + 20), (self.x + 30, self.y + 50)), 3)

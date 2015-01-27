import pygame

class Lander:

  def __init__(self):

    self.x = 50.0
    self.y = 50.0

    self.speed_x = 0.0
    self.speed_y = 0.0

    self.size = 20.0
    self.color = (255, 255, 255)

  def on_loop(self, gravity):

    self.x = self.x + self.speed_x

    self.speed_y = self.speed_y + gravity
    self.y = self.y + self.speed_y

  def on_render(self, screen):
    pygame.draw.polygon(screen, self.color, (
      (self.x, self.y),
      (self.x + self.size, self.y - self.size),
      (self.x + self.size * 2, self.y - self.size),
      (self.x + self.size * 3, self.y)
      ), 1)

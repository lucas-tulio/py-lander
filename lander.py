import pygame

class Lander:

  def __init__(self):

    self.x = 50.0
    self.y = 50.0

    self.speed_x = 0.1
    self.speed_y = 0.0

    self.acceleration_x = 0.0003
    self.acceleration_y = 0.0005

    self.color = (255, 255, 255)

  def on_loop(self, gravity_acceleration):

    # Add gravity to speed Y
    self.speed_y = self.speed_y + gravity_acceleration
    
    # Ship's speed
    self.x = self.x + self.speed_x
    self.y = self.y + self.speed_y

  def on_render(self, screen):
    pygame.draw.polygon(screen, self.color, (
      
      # Ship body
      (self.x, self.y),
      (self.x, self.y - 8.0),
      (self.x + 4.0, self.y - 12.0),
      (self.x + 8.0, self.y - 12.0),
      (self.x + 12.0, self.y - 8.0),
      (self.x + 12.0, self.y)
      ), 1)

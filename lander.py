import pygame

class Lander:

  def __init__(self):

    self.x = 50.0
    self.y = 50.0
    self.size = 4.0

    self.speed_x = 0.1
    self.speed_y = 0.0

    self.acceleration_x = 0.0005
    self.acceleration_y = 0.0005

    self.color = (255, 255, 255)

  def on_loop(self, gravity_acceleration, holding_right, holding_left, holding_up):

    # Add gravity to speed Y
    self.speed_y = self.speed_y + gravity_acceleration
    
    # Check which keys are being pressed and change the ship's speed accordingly
    if holding_right:
      self.speed_x = self.speed_x + self.acceleration_x
    elif holding_left:
      self.speed_x = self.speed_x - self.acceleration_x
    if holding_up:
      self.speed_y = self.speed_y - self.acceleration_y

    # Ship's speed
    self.x = self.x + self.speed_x
    self.y = self.y + self.speed_y

  def on_render(self, screen):

    pygame.draw.polygon(screen, self.color, (
      (self.x, self.y),
      (self.x, self.y - self.size*2),
      (self.x + self.size, self.y - self.size*3),
      (self.x + self.size*2, self.y - self.size*3),
      (self.x + self.size*3, self.y - self.size*2),
      (self.x + self.size*3, self.y)
      ), 1)

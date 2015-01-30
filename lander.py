import pygame

class Lander:

  def __init__(self):

    self.x = -10.0
    self.y = 50.0
    self.size = 4.0
    self.fuel = 100.0
    self.fuel_delta = 0.1

    self.speed_x = 1.0
    self.speed_y = 0.0

    self.acceleration_x = 0.02
    self.acceleration_y = 0.02

    self.is_rekt = False
    self.is_landed = False

    # Colors
    self.normal_color = (255, 255, 255)
    self.out_of_fuel_color = (128, 128, 0)
    self.rekt_color = (255, 0, 0)
    self.current_color = self.normal_color

  def on_loop(self, gravity_acceleration, holding_right, holding_left, holding_up):

    # Add gravity to speed Y
    self.speed_y = self.speed_y + gravity_acceleration

    # Check which keys are being pressed and change the ship's speed accordingly
    if self.fuel > 0.0:
      if holding_right:
        self.fuel = self.fuel - self.fuel_delta
        self.speed_x = self.speed_x + self.acceleration_x
      elif holding_left:
        self.fuel = self.fuel - self.fuel_delta
        self.speed_x = self.speed_x - self.acceleration_x
      if holding_up:
        self.fuel = self.fuel - self.fuel_delta
        self.speed_y = self.speed_y - self.acceleration_y

    # Fuel status
    if self.is_rekt:
      self.current_color = self.rekt_color
    elif self.fuel <= 0:
      self.current_color = self.out_of_fuel_color
    else:
      self.current_color = self.normal_color

    # Ship's speed
    self.x = self.x + self.speed_x
    self.y = self.y + self.speed_y

  def on_render(self, screen):
    
    pygame.draw.polygon(screen, self.current_color, (
    (self.x, self.y),
    (self.x, self.y - self.size*2),
    (self.x + self.size, self.y - self.size*3),
    (self.x + self.size*2, self.y - self.size*3),
    (self.x + self.size*3, self.y - self.size*2),
    (self.x + self.size*3, self.y)
    ), 0)

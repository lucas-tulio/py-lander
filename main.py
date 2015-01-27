import pygame
from pygame.locals import *
from lander import Lander
from random import randint
from pygame import freetype

class App:

  def __init__(self):

    self._running = True
    self.screen = None
    self.size = self.width, self.height = 1200, 600
    self.clock = pygame.time.Clock()
    freetype.init()
    self.font = pygame.font.SysFont("monospace", 18)

    # Basic settings
    self.gravity = 0.01
    self.ground_height = 60

    # Controls
    self.holding_left = False
    self.holding_right = False
    self.holding_up = False

    # Space
    self.space = []
    for i in range(0, 500):
      self.space.append((randint(0, self.width), randint(0, self.height)))

  #
  # Game setup
  #
  def on_init(self):

    pygame.init()
    self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
    self._running = True
    pygame.display.set_caption("py-lander")

    # Create our Lander
    self.lander = Lander()

  #
  # Process input
  #
  def on_event(self, event):

    # Key Down
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        self.holding_left = True
      elif event.key == pygame.K_RIGHT:
        self.holding_right = True
      elif event.key == pygame.K_UP:
        self.holding_up = True

      elif event.key == pygame.K_r:
        self.on_init()

    # Key Up
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        self.holding_left = False
      elif event.key == pygame.K_RIGHT:
        self.holding_right = False
      elif event.key == pygame.K_UP:
        self.holding_up = False
    elif event.type == pygame.QUIT:
      self._running = False

  #
  # Main game logic
  #
  def on_loop(self):

    self.clock.tick(60)

    # Ship logic (including controls and movement)
    if not self.lander.is_rekt:
      self.lander.on_loop(self.gravity, self.holding_right, self.holding_left, self.holding_up)

    # Check ground collision
    if self.lander.y >= self.height - self.ground_height:
      
      # Check if rekt
      if self.lander.speed_y > 1.0:
        self.lander.is_rekt = True

      # Stop
      self.lander.speed_x = 0
      self.lander.speed_y = 0

  #
  # Render
  #
  def on_render(self):

    # Clear screen
    self.screen.fill((0, 0, 0))

    # Draw space
    for star in self.space:
      self.screen.set_at((star[0], star[1]), (255, 255, 255))

    # Draw lander
    self.lander.on_render(self.screen)

    # Draw ground
    pygame.draw.rect(self.screen, (255, 255, 255),
      (0, self.height - self.ground_height, self.width, self.height))

    # Draw message if rekt
    if self.lander.is_rekt:
      text = self.font.render("Rekt! Press R to try again", 1, (255, 255, 255))
      text_rect = text.get_rect()
      text_rect.centerx = self.width / 2
      text_rect.centery = self.height / 8
      self.screen.blit(text, text_rect)

    # Draw UI
    speed_x_text = self.font.render("speed_x: " + str(self.lander.speed_x), 1, (255, 255, 255))
    speed_y_text = self.font.render("speed_y: " + str(self.lander.speed_y), 1, (255, 255, 255))
    fuel_text = self.font.render("fuel: " + str(self.lander.fuel), 1, (255, 255, 255))
    self.screen.blit(speed_x_text, (0, 0))
    self.screen.blit(speed_y_text, (0, 20))
    self.screen.blit(fuel_text, (0, 40))

    pygame.display.update()

  #
  # Ends the game
  #
  def on_cleanup(self):
    pygame.quit()

  #
  # Starts the game
  #
  def on_execute(self):
    if self.on_init() == False:
      self._running = False

    while(self._running):
      for event in pygame.event.get():
        self.on_event(event)
      self.on_loop()
      self.on_render()
    self.on_cleanup()

if __name__ == "__main__":
  theApp = App()
  theApp.on_execute()

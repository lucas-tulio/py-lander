import pygame
from pygame.locals import *
from lander import Lander

class App:

  def __init__(self):

    self._running = True
    self.screen = None
    self.size = self.weight, self.height = 640, 400

    # Gravity
    self.gravity = 0.0001

    # Controls
    self.holding_left = False
    self.holding_right = False
    self.holding_up = False

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

    # Ship logic (including controls and movement)
    self.lander.on_loop(self.gravity, self.holding_right, self.holding_left, self.holding_up)

    # Check ground collision
    if self.lander.y >= 300:
      self.lander.speed_x = 0
      self.lander.speed_y = 0

  #
  # Render
  #
  def on_render(self):

    self.screen.fill((0, 0, 0))

    # Draw ground
    pygame.draw.rect(self.screen, (255, 255, 255), (0, 300, 640, 400))

    # Draw lander
    self.lander.on_render(self.screen)

    pygame.display.flip()

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

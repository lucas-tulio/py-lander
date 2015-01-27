import pygame
from pygame.locals import *
from lander import Lander

class App:

  def __init__(self):

    self._running = True
    self.screen = None
    self.size = self.weight, self.height = 640, 400

    self.gravity = 0.0001
    self.moving_left = False
    self.moving_right = False
    self.moving_up = False
    self.moving_down = False

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
        self.moving_left = True
      elif event.key == pygame.K_RIGHT:
        self.moving_right = True
      elif event.key == pygame.K_UP:
        self.moving_up = True
      elif event.key == pygame.K_DOWN:
        self.moving_down = True

    # Key Up
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        self.moving_left = False
      elif event.key == pygame.K_RIGHT:
        self.moving_right = False
      elif event.key == pygame.K_UP:
        self.moving_up = False
      elif event.key == pygame.K_DOWN:
        self.moving_down = False
    elif event.type == pygame.QUIT:
      self._running = False

  #
  # Main game logic
  #
  def on_loop(self):

    if self.moving_left:
      self.lander.speed_x = self.lander.speed_x - 0.001
    elif self.moving_right:
      self.lander.speed_x = self.lander.speed_x + 0.001
    elif self.moving_up:
      self.lander.speed_y = self.lander.speed_y - 0.001
    elif self.moving_down:
      self.lander.speed_y = self.lander.speed_y + 0.001

    self.lander.on_loop(self.gravity)

    # Check ground collision
    if self.lander.y >= 300:
      self.lander.speed_x = 0
      self.lander.speed_y = 0

  #
  # Render
  #
  def on_render(self):

    self.screen.fill((0, 0, 0))

    # Drag ground
    pygame.draw.rect(self.screen, (255, 255, 255), (0, 300, 640, 400))

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

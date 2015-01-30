import pygame
from lander import Lander
from random import randint
from pygame import mixer

class App:

  def __init__(self):

    self._running = True
    self.screen = None
    self.size = self.width, self.height = 600, 300
    self.clock = pygame.time.Clock()

  #
  # Game setup
  #
  def on_init(self):

    pygame.init()
    self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
    self._running = True
    pygame.display.set_caption("py-lander")

    # Start sounds
    pygame.mixer.init()
    self.engine_sound = pygame.mixer.Sound("./sounds/engine.wav")
    self.landing_sound = pygame.mixer.Sound("./sounds/landing.wav")
    self.rekt_sound = pygame.mixer.Sound("./sounds/rekt.wav")
    self.played_landing_sound = False
    self.played_rekt_sound = False

    self.font = pygame.font.SysFont("monospace", 18)

    # Create our Lander
    self.lander = Lander()

    # Score multiplier
    self.score_multiplier = 1.0
    self.can_multiply = True

    # Basic settings
    self.gravity = 0.01
    self.ground_height = 30

    # Controls
    self.holding_left = False
    self.holding_right = False
    self.holding_up = False

    # Space
    self.space = []
    for i in range(0, 500):
      self.space.append((randint(0, self.width), randint(0, self.height)))

  #
  # Process input
  #
  def on_event(self, event):

    # Key Down
    if event.type == pygame.KEYDOWN:

      self.can_multiply = False

      if not self.lander.is_rekt and not self.lander.is_landed:
        if event.key == pygame.K_LEFT:
          self.engine_sound.play(loops=1)
          self.holding_left = True
        elif event.key == pygame.K_RIGHT:
          self.engine_sound.play(loops=1)
          self.holding_right = True
        elif event.key == pygame.K_UP:
          self.engine_sound.play(loops=1)
          self.holding_up = True

      if event.key == pygame.K_r:
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

    # Score multiplier
    if self.can_multiply:
      self.score_multiplier = self.score_multiplier + 0.01

    # Ship logic (including controls and movement)
    if not self.lander.is_rekt and not self.lander.is_landed:
      self.lander.on_loop(self.gravity, self.holding_right, self.holding_left, self.holding_up)

    # Check ground collision
    if not (self.lander.is_rekt or self.lander.is_landed) and self.lander.y >= self.height - self.ground_height:

      # Check if rekt
      if self.lander.speed_y >= 1.0 or self.lander.speed_x >= 1.0:
        
        self.lander.is_rekt = True
        self.lander.current_color = self.lander.rekt_color
        self.rekt_sound.play()

      else:

        self.lander.is_landed = True

        if not self.played_landing_sound:
          self.engine_sound.stop()
          self.landing_sound.play()
          self.played_landing_sound = True

      # Stop
      self.lander.speed_x = 0
      self.lander.speed_y = 0

  #
  # Render
  #
  def on_render(self):

    # Clear screen
    self.screen.fill((0, 0, 0))

    # Draw the score multiplier
    multiplier_text = self.font.render("Score x" + str(self.score_multiplier), 1, (255, 255, 255))
    self.screen.blit(multiplier_text, (20, 40))

    # Draw space
    for star in self.space:
      self.screen.set_at((star[0], star[1]), (255, 255, 255))

    # Draw lander
    self.lander.on_render(self.screen)

    # Draw ground
    pygame.draw.rect(self.screen, (255, 255, 255),
      (0, self.height - self.ground_height, self.width, self.height))

    # Show rekt message
    if self.lander.is_rekt:

      text = self.font.render("Rekt! Press R to try again", 1, (255, 255, 255))
      text_rect = text.get_rect()
      text_rect.centerx = self.width / 2
      text_rect.centery = 80
      self.screen.blit(text, text_rect)

    elif self.lander.is_landed:

      text = self.font.render("A perfect landing!", 1, (255, 255, 255))
      text_rect = text.get_rect()
      text_rect.centerx = self.width / 2
      text_rect.centery = 80
      self.screen.blit(text, text_rect)

      fuel_score = int(self.lander.fuel * 10)
      total_score = int(fuel_score * self.score_multiplier) * 10

      text = self.font.render(str(fuel_score) + " fuel x " + str(self.score_multiplier), 1, (255, 255, 255))
      text_rect = text.get_rect()
      text_rect.centerx = self.width / 2
      text_rect.centery = 120
      self.screen.blit(text, text_rect)

      text = self.font.render("Score: " + str(total_score), 1, (255, 255, 255))
      text_rect = text.get_rect()
      text_rect.centerx = self.width / 2
      text_rect.centery = 140
      self.screen.blit(text, text_rect)

    # Draw the fuel bar
    pygame.draw.rect(self.screen, (255, 255, 255), (20, 20, ((self.width - 40) * (self.lander.fuel / 25.0)), 20), 0)

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

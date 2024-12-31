import pygame
from constants import SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):
  def __init__(self, position, velocity):
    super().__init__(position.x, position.y, SHOT_RADIUS)
    self.velocity = velocity

  def draw(self, screen):
    color = (255, 255, 255)
    pygame.draw.circle(screen, color, self.position, SHOT_RADIUS, 2)

  def update(self, dt):
    self.position += self.velocity * dt

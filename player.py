import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):
  def __init__(self, x, y,):
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = 0

  def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]
  
  def rotate(self, direction, dt):
    self.rotation += direction * PLAYER_TURN_SPEED * dt

  def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1, dt)
        if keys[pygame.K_d]:
            self.rotate(1, dt)
        if keys[pygame.K_w]:
            self.move(dt, 1)
        if keys[pygame.K_s]:
           self.move(dt, -1)
        if keys[pygame.K_SPACE]:
           self.shoot()
  def move(self, dt, direction):
     forward = pygame.Vector2(0, 1).rotate(self.rotation)
     self.position += forward * PLAYER_SPEED * dt * direction
  
  def shoot(self):
     velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
     shot = Shot(self.position, velocity)
     return shot

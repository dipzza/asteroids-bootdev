import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    random_angle = random.uniform(20, 50)
    new_velocity_a = self.velocity.rotate(random_angle) * 1.2
    new_velocity_b = self.velocity.rotate(-random_angle) * 1.2
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    
    new_asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
    new_asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
    new_asteroid_a.velocity = new_velocity_a
    new_asteroid_b.velocity = new_velocity_b


import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
  dt = 0
  pygame.init()  
  clock = pygame.time.Clock()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
  updatables = pygame.sprite.Group()
  drawables = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  Player.containers = (updatables, drawables)
  Asteroid.containers = (asteroids, updatables, drawables)
  AsteroidField.containers = (updatables)
  Shot.containers = (shots, updatables, drawables)

  center_x = SCREEN_WIDTH / 2
  center_y = SCREEN_HEIGHT / 2
  player = Player(center_x, center_y)
  AsteroidField()
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
      
    screen.fill((0, 0, 0))

    for updatable in updatables:
      updatable.update(dt)

    for asteroid in asteroids:
      if (asteroid.collides(player)):
        print("Game over!")
        return
      for bullet in shots:
        if (bullet.collides(asteroid)):
          asteroid.split()
          bullet.kill()

    for drawable in drawables:
      drawable.draw(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()
import pygame
from constants import *
from player import PLayer
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	fps_clock = pygame.time.Clock()


	# groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	AsteroidField()

	PLayer.containers = (updatable, drawable)
	PLayer(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	dt = 0

	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		updatable.update(dt)

		screen.fill((0, 0, 0))

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()

		# limit timeframe to 60 fps
		dt = fps_clock.tick(60) / 1000

if __name__ == "__main__":
	main()

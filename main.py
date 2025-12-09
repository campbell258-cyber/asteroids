import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    BLACK = (0, 0, 0)

    running = True
    while running:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)

        # Player–asteroid collisions
        for asteroid in list(asteroids):
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                pygame.quit()
                sys.exit()

        # Shot–asteroid collisions
        for shot in list(shots):
            for asteroid in list(asteroids):
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.kill()
                    shot.kill()
                    break  # this shot is gone; no need to check more asteroids

        screen.fill(BLACK)

        # If your sprites implement draw(screen):
        for sprite in drawable:
            sprite.draw(screen)

        # Or, if you use pygame's Group.draw and sprites have image/rect:
        # drawable.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000.0

    pygame.quit()


if __name__ == "__main__":
    main()
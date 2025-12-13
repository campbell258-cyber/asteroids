import pygame, random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        first_asteroid_direction = self.velocity.rotate(angle)
        second_asteroid_direction = self.velocity.rotate(-angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        x = self.position[0]
        y = self.position[1]
        asteroid_one = Asteroid(x, y, new_asteroid_radius)
        asteroid_one.velocity = first_asteroid_direction * 1.2
        asteroid_two = Asteroid(x, y, new_asteroid_radius)
        asteroid_two.velocity = second_asteroid_direction * 1.2
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SCORE_INCREMENT
import pygame
import random
from score import Score

class Asteroid(CircleShape):
    containers = None
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        Score.game_score += SCORE_INCREMENT
        print(f"New game score: {Score.game_score}")
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20.0, 50.0)
            v1 = self.velocity.rotate(random_angle)
            v2 = self.velocity.rotate(random_angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = v1 * 1.2
            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a2.velocity = v2 * 1.2

        
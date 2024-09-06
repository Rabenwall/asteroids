from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN, SHOT_RADIUS, SHOT_RH_COUNT, SHOT_RH_ACTIVATE_COUNT
from constants import SHOT_RADIUS, SHOT_RH_COUNT, SHOT_RH_ACTIVATE_COUNT
import pygame
from shot import Shot
import random

class Player(CircleShape):
    containers = None
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.shot_count = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        if self.shot_timer > 0:
            self.shot_timer -= dt
        random_angle = random.uniform(20.0, 50.0)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            if self.shot_timer <= 0:
                if self.shot_count == SHOT_RH_ACTIVATE_COUNT:
                    self.roundhouse_shot()
                    self.shot_count = 0
                else:
                    self.shoot()


    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
        self.shot_count += 1

    def roundhouse_shot(self):
        angle_diff = 360 / SHOT_RH_COUNT
        shot_angle = self.rotation + angle_diff / 2
        for i in range(SHOT_RH_COUNT):
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS * 3, "red")
            shot.velocity = pygame.Vector2(0, 1).rotate(shot_angle) * PLAYER_SHOOT_SPEED * 0.5
            shot_angle += angle_diff
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
        

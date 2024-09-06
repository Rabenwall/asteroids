import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    fps = 60
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # Object groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for to_update in updatable:
            to_update.update(dt)
        for actual_asteroid in asteroids:
            if actual_asteroid.collidesWith(player):
                print("Game over!")
                return
            for actual_shot in shots:
                if actual_asteroid.collidesWith(actual_shot):
                    actual_asteroid.split()
                    actual_shot.kill()
                    break
        for to_draw in drawable:
            to_draw.draw(screen)
        pygame.display.flip()
        dt= clock.tick(fps) / 1000

if __name__ == "__main__":
    main()
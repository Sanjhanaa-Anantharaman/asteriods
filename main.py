import pygame # type: ignore
from constants import SCREEN_WIDTH, SCREEN_HEIGHT # type: ignore
from logger import log_state # type: ignore
from player import Player # type: ignore
from asteroid import Asteroid # type: ignore
from asteroidfield import AsteroidField # type: ignore
from logger import log_event # type: ignore
import sys
from shot import Shot # type: ignore

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()
    Shot.containers = (shots, updatable, drawable)
    player = Player(x, y)
    while 1:
        log_state()
        dt = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
        screen.fill("black")
        for drawable_sprite in drawable:
            drawable_sprite.draw(screen)
        pygame.display.flip()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()

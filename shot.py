from circleshape import CircleShape
import pygame # type: ignore
class Shot(CircleShape):
    def __init__(self, x, y, velocity_x, velocity_y):
        super().__init__(x, y, 5)
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
    def update(self, dt):
        self.position.x += self.velocity_x * dt
        self.position.y += self.velocity_y * dt
        if (self.position.x < 0 or self.position.x > 1280 or
            self.position.y < 0 or self.position.y > 720):
            self.kill()
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)  
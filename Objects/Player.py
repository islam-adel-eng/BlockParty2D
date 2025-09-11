import pygame

class player():
    def __init__(self, color, radius, posX, posY, speed):
        self.color = color
        self.radius = radius
        self.posX = posX
        self.posY = posY
        self.speed = speed

    def draw(self, surface, dt, UI_h, round_state):
        Circle = pygame.draw.circle(surface, self.color, [self.posX, self.posY], self.radius)

        keys = pygame.key.get_pressed()
        if round_state == 1:
            if keys[pygame.K_w] and self.posY > self.radius + UI_h:
                self.posY -= self.speed * dt
            if keys[pygame.K_s] and self.posY < surface.get_height() - self.radius:
                self.posY += self.speed * dt

            if keys[pygame.K_a] and self.posX > self.radius:
                self.posX -= self.speed * dt
            if keys[pygame.K_d] and self.posX < surface.get_width() - self.radius:
                self.posX += self.speed * dt

        surface.blit(surface, Circle, Circle)

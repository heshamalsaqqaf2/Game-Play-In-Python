import pygame
import random
from game_objects import GameObject


class Ball(GameObject):
    def __init__(self, x, y, diameter, color):
        super().__init__(x, y, diameter, diameter, color, speed=4)
        self.speed_x = self.speed * random.choice([-1, 1])
        self.speed_y = self.speed * random.choice([-1, 1])
        self.sound = pygame.mixer.Sound("")

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)

    def update(self, screen_hieght):
        self.move(self.speed_x, self.speed_y)

        if self.rect.top <= 0 or self.rect.bottom >= screen_hieght:
            self.speed_y *= -1
            self.sound.play()

    def reset_position(self, screen_width, screen_hieght):
        pass

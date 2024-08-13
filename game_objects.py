import pygame
from abc import ABC, abstractmethod


class GameObject(ABC):
    """This is abstract class in objects basies"""

    def __init__(self, x, y, width, height, color, speed=0):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = speed

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def update(self):
        pass

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def check_collision(self, other):
        return self.rect.colliderect(other.rect)

from draw_engine.config import RECTANGLE_DEFAULT_SIZE, LINE_WIDTH, CIRCLE_CENTER, CIRCLE_RADIUS, \
    TRIANGLE_DEFAULT_SIZE
from draw_engine.engine.base import Primitive
import pygame


class Rectangle(Primitive):
    size = RECTANGLE_DEFAULT_SIZE

    def draw(self, screen):
        super().draw()
        pygame.draw.rect(screen, self.color, self.size, width=LINE_WIDTH)


class Circle(Primitive):
    center = CIRCLE_CENTER
    radius = CIRCLE_RADIUS

    def draw(self, screen):
        super().draw()
        pygame.draw.circle(screen, self.color, self.center, self.radius, width=LINE_WIDTH)


class Triangle(Primitive):
    size = TRIANGLE_DEFAULT_SIZE

    def draw(self, screen):
        super().draw()
        pygame.draw.polygon(screen, self.color, self.size, width=LINE_WIDTH)

import time

import pygame

from draw_engine.config import SCREEN_WIDTH, SCREEN_HEIGHT
from draw_engine.engine.base import Primitive
from draw_engine.engine.constants import COLOR_MAP


class Engine2D:

    def __init__(self):
        self.run = True
        self.figure_color = COLOR_MAP[5]  # white
        self.canvas_color = COLOR_MAP[2]  # blue
        self.canvas = list()
        self.screen = self._init_screen()

    def _init_screen(self):
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Drawing shapes")
        screen.fill(self.canvas_color)
        pygame.display.update()
        return screen

    def set_figure_color(self, color: int):
        self.figure_color = COLOR_MAP[color]

    def add(self, figure):
        if issubclass(figure, Primitive):
            self.canvas.append(figure(color=self.figure_color))
        else:
            raise Exception("Object added to canvas is not a geometric figure")

    def clear_canvas(self):
        self.canvas = list()
        self.screen.fill(self.canvas_color)
        pygame.display.update()

    def draw(self):
        for item in self.canvas:
            item.draw(self.screen)
            pygame.display.update()
            time.sleep(1)

        self.clear_canvas()
        time.sleep(2)
        self.shutdown()

    def shutdown(self):
        self.run = False

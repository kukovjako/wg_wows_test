import re
import time

import pygame

from draw_engine.config import SCREEN_WIDTH, SCREEN_HEIGHT
from draw_engine.engine.base import Primitive
from draw_engine.engine.constants import STRING_STRIPPING_PATTERN, COLOR_MAP
from draw_engine.engine.primitives import Rectangle, Circle, Triangle


class Engine2D:
    FIGURES_MAP = {1: Rectangle, 2: Circle, 3: Triangle}

    def __init__(self):
        self.run = True
        self.figure_color = COLOR_MAP[4]  # black
        self.canvas_color = COLOR_MAP[5]  # white
        self.canvas = list()
        self.screen = self._init_screen()

    def _init_screen(self):
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Drawing shapes")
        screen.fill(self.canvas_color)
        pygame.display.update()
        return screen

    def set_figure_color(self, input_color: str):
        _str = re.sub(STRING_STRIPPING_PATTERN, "", input_color)
        try:
            self.figure_color = COLOR_MAP[int(_str[0])]
        except (KeyError, IndexError):
            print("No such color. Using Black")

    def _add(self, figure):
        if issubclass(figure, Primitive):
            self.canvas.append(figure(color=self.figure_color))
        else:
            raise Exception("Object added to canvas is not a geometric figure")

    def add_figures_to_canvas(self, figures_input: str):
        _str = re.sub(STRING_STRIPPING_PATTERN, "", figures_input)
        if _str:
            for num in _str:
                try:
                    self._add(self.FIGURES_MAP[int(num)])
                except KeyError:
                    print("Wrong number entered: No such figure")
        else:
            print("No figures were selected, shutting down")
            self.shutdown()

    def clear_canvas(self):
        print("Clearing canvas")
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

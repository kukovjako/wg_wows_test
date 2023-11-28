import re
import time

import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT
from engine.base import Primitive
from engine.constants import COLOR_MAP, GET_INT_PATTERN
from engine.primitives import Rectangle, Circle, Triangle


class Engine2D:
    FIGURES_MAP = {1: Rectangle, 2: Circle, 3: Triangle}

    def __init__(self, screen=None):
        self.run = True
        self.figure_color = COLOR_MAP[4]  # black
        self.canvas_color = COLOR_MAP[5]  # white
        self.canvas = list()
        self.screen = screen if screen else self._init_screen()

    def _init_screen(self):
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Drawing shapes")
        screen.fill(self.canvas_color)
        pygame.display.update()
        return screen

    def set_figure_color(self, input_color: str):
        # stripping user input
        _str = re.sub(GET_INT_PATTERN, "", input_color)
        try:
            self.figure_color = COLOR_MAP[int(_str[0])]
        except (KeyError, IndexError):
            print("No such color. Using Black")

    def _add(self, figure):
        if issubclass(figure, Primitive):
            self.canvas.append(figure(color=self.figure_color))
        else:
            # just in case
            raise Exception("Object added to canvas is not a geometric figure")

    def add_figures_to_canvas(self, figures_input: str):
        # stripping user input
        _str = re.sub(GET_INT_PATTERN, "", figures_input)
        if _str:
            for num in _str:
                try:
                    self._add(self.FIGURES_MAP[int(num)])
                except KeyError:
                    print("Wrong number entered: No such figure")
        else:
            print("No figures were selected, shutting down")
            self._shutdown()

    def clear_canvas(self):
        print("Clearing canvas")
        self.canvas = list()
        self.screen.fill(self.canvas_color)
        pygame.display.update()

    def draw(self):
        # Drawing happens too fast to be user-friendly, so I added sleeps
        for item in self.canvas:
            item.draw(self.screen)
            pygame.display.update()
            time.sleep(1)

        self.clear_canvas()
        time.sleep(1)
        self._shutdown()

    def _shutdown(self):
        self.run = False

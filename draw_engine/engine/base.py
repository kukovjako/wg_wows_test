
from draw_engine.engine.constants import COLOR_MAP


class Primitive:
    color = COLOR_MAP[5]  # White

    def __init__(self, color=None):
        self.color = color if color else self.color

    def draw(self, screen=None):
        print(f"Drawing {self.__class__.__name__}: with ") # if color - color   attrs in __dict__?
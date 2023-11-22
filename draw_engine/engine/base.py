from draw_engine.engine.constants import COLOR_NAMES_MAP


class Primitive:
    def __init__(self, color):
        self.color = color

    def draw(self, screen=None):
        attrs_to_print = dict()
        for k, v in self.__dict__.items():
            # for printing color name instead of tuple with numbers
            if k == "color":
                v = COLOR_NAMES_MAP[self.color]
            attrs_to_print[k] = v

        print(f"Drawing {self.__class__.__name__}: with {attrs_to_print}")

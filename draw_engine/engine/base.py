
class Primitive:

    def __init__(self, color=None):
        self.color = color

    def draw(self, screen=None):
        print(f"Drawing {self.__class__.__name__}: with {self.__dict__}")
        # if color - color   attrs in __dict__?
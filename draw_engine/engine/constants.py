from draw_engine.engine.primitives import Rectangle, Circle, Triangle

COLOR_MAP = {
    1: (255, 0, 0),
    2: (0, 0, 255),
    3: (0, 255, 0),
    4: (0, 0, 0),
    5: (255, 255, 255),
}

# for printing out
COLOR_NAMES_MAP = {
    1: "red",
    2: "blue",
    3: "green",
    4: "black",
    5: "white",
}

FIGURES_MAP = {
    1: Rectangle,
    2: Circle,
    3: Triangle
}

STRING_STRIPPING_PATTERN = "(\[\d+\]|\n)"

import pygame

from engine.engine import Engine2D

if __name__ == "__main__":
    figures_to_draw = input(
        "To add figures to canvas, enter numbers in one line"
        "\n1 - Rectangle "
        "\n2 - Circle "
        "\n3 - Triangle"
        "\n"
    )
    printing_color = input(
        "Choose color or leave blank for black:"
        "\n1 - Red"
        "\n2 - Blue"
        "\n3 - Green"
        "\n"
    )
    pygame.init()
    engine = Engine2D()
    engine.set_figure_color(printing_color)
    engine.add_figures_to_canvas(figures_to_draw)
    while engine.run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                engine.run = False
        engine.draw()
    pygame.quit()

import pygame

from draw_engine.engine.engine import Engine2D
from draw_engine.engine.primitives import Rectangle, Circle, Triangle

if __name__ == "__main__":
    running = True
    pygame.init()
    engine = Engine2D()
    engine.add(Rectangle)
    engine.add(Circle)
    engine.add(Triangle)
    while engine.run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        engine.draw()
    pygame.quit()





from unittest.mock import patch, Mock

import pytest
import pygame
from engine.constants import COLOR_MAP
from engine.primitives import Rectangle, Circle, Triangle


class TestFigures:

    @pytest.mark.parametrize('figure_obj, obj_to_patch, expected_response', [
        (
                Rectangle,
                "rect",
                "Drawing Rectangle: with {'color': 'red', 'size': (200, 100, 150, 150)}\n"
        ),
        (
                Circle,
                "circle",
                "Drawing Circle: with {'color': 'red', 'center': (300, 200), 'radius': 75}\n"
        ),
        (
                Triangle,
                "polygon",
                "Drawing Triangle: with "
                "{'color': 'red', 'size': ((200, 100), (250, 150), (150, 200))}\n"
        ),
    ])
    def test_figure_draw(self, figure_obj, obj_to_patch, expected_response, capfd):
        with patch.object(pygame.draw, obj_to_patch, Mock()):
            figure = figure_obj(color=COLOR_MAP[1])  # Red
            figure.draw(screen=None)
            out, _ = capfd.readouterr()
            assert out == expected_response


class TestEngine:

    def test_add_figures_to_canvas(self, setup):
        engine = setup
        engine.add_figures_to_canvas("123")
        assert len(engine.canvas) == 3
        assert isinstance(engine.canvas[0], Rectangle)
        assert isinstance(engine.canvas[1], Circle)
        assert isinstance(engine.canvas[2], Triangle)

    def test_add_figures_to_canvas_empty_input(self, setup, capfd):
        engine = setup
        engine.add_figures_to_canvas("")
        out, _ = capfd.readouterr()
        assert len(engine.canvas) == 0
        assert out == "No figures were selected, shutting down\n"
        assert engine.run is False

    def test_add_figures_to_canvas_random_str(self, setup):
        engine = setup
        engine.add_figures_to_canvas("test_string_3/.,#$%%@2_testtest")
        assert isinstance(engine.canvas[0], Triangle)
        assert isinstance(engine.canvas[1], Circle)
        assert len(engine.canvas) == 2

    def test_set_color(self, setup):
        engine = setup
        engine.set_figure_color("1")
        engine.add_figures_to_canvas("1")
        assert engine.figure_color == COLOR_MAP[1]  # Red
        assert engine.canvas[0].color == engine.figure_color

    def test_set_color_random_input(self, setup):
        engine = setup
        engine.set_figure_color("lfksdj3flksdj''///'*&^%#&^&flksdj123213")
        assert engine.figure_color == COLOR_MAP[3]  # Green

    def test_set_color_no_input(self, setup):
        engine = setup
        engine.set_figure_color("")
        assert engine.figure_color == COLOR_MAP[4]  # Black

    def test_clear_canvas(self, setup):
        engine = setup
        engine.add_figures_to_canvas("1")
        with patch.object(pygame.display, "update", Mock()):
            engine.clear_canvas()
            assert len(engine.canvas) == 0

    def test_shutdown(self, setup, capfd):
        engine = setup
        assert engine.run is True
        engine._shutdown()
        assert engine.run is False

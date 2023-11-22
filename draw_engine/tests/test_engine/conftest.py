from unittest.mock import Mock
import pytest

from draw_engine.engine.engine import Engine2D


@pytest.fixture(scope="function")
def setup():
    screen = Mock()
    engine = Engine2D(screen)
    return engine


@pytest.fixture(scope="module", autouse=True)
def divider_module(request):
    print("\n======== MODULE:[%s] ========" % request.module.__name__)

    def fin():
        print("\n======== FINISH MODULE:[%s] ========" % request.module.__name__)

    request.addfinalizer(fin)


@pytest.fixture(scope="function", autouse=True)
def newline_function(request):
    print("\n")





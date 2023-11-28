import pytest
from base.common import wiki_table_setup


@pytest.fixture(scope="session", autouse=True)
def setup():
    table = wiki_table_setup()
    return table


@pytest.fixture(scope="module", autouse=True)
def divider_module(request):
    print("\n======== MODULE:[%s] ========\n" % request.module.__name__)

    def fin():
        print("\n======== FINISH MODULE:[%s] ========" % request.module.__name__)

    request.addfinalizer(fin)

from wiki_test.base.config import POPULAR_LANGUAGES_URL
from wiki_test.base.parser import WikiParser
from wiki_test.base.table_dataclasses import (
    WikiPopularLanguagesTable,
    WikiPopularLanguagesTableRow,
)


def wiki_table_setup() -> WikiPopularLanguagesTable:
    page = WikiParser(POPULAR_LANGUAGES_URL)
    popular_websites_table = page.get_popular_websites_table_as_dataclass()
    return popular_websites_table


def build_error_message(row: WikiPopularLanguagesTableRow, control_sum):
    return (
        "%s (Frontend:%s|Backend:%s) has %s unique visitors per month. "
        "(Expected more than %s)"
        % (row.website, row.frontend, row.backend, row.popularity, control_sum)
    )

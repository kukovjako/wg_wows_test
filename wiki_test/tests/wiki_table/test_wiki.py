import pytest

from wiki_test.base.common import build_error_message


class TestWikiPopularWebsitesTable:
    @pytest.mark.parametrize(
        "control_sum",
        [
            10**7,
            1.5 * 10**7,
            5 * 10**7,
            10**8,
            5 * 10**8,
            10**9,
            1.5 * 10**9,
        ],
    )
    def test_websites_popularity(self, setup, control_sum):
        """
        1. Get "Programming languages used in most popular websites*" table from wiki page
        2. Assert popularity data is not less than expected in test params
        """
        errors = []
        wiki_table = setup
        for row in wiki_table.rows:
            if row.popularity < control_sum:
                errors.append(build_error_message(row, control_sum))
        try:
            assert len(errors) == 0
        except AssertionError:
            for error in errors:
                print("\n" + error)
            raise AssertionError("Test failed")

import re
from typing import List

import requests
from bs4 import BeautifulSoup

from base.config import POPULAR_WEBSITES_TABLE_NAME, TABLE_CELLS_STRIPPING_PATTERN
from base.table_dataclasses import (
    WikiPopularLanguagesTableRow,
    WikiPopularLanguagesTable,
)


class WikiParser:
    def __init__(self, url):
        self.page = self._get_page(url)

    @staticmethod
    def _get_page(url: str) -> BeautifulSoup:
        response = requests.get(url).content
        return BeautifulSoup(response, features="html.parser")

    @staticmethod
    def get_row_readable_data(rows) -> List:
        pattern = re.compile(TABLE_CELLS_STRIPPING_PATTERN)
        for row in rows:
            useful_data = []
            cells = row.find_all("td")
            for cell in cells:
                if cell.text:
                    useful_data.append(pattern.sub("", cell.text))
                elif cell.title:
                    useful_data.append(pattern.sub("", cell.title))
                else:
                    useful_data.append(None)
            yield useful_data

    def _get_popular_websites_table_as_rows(self):
        table = self.page.find(
            "caption", string=re.compile(POPULAR_WEBSITES_TABLE_NAME)
        ).parent.find("tbody")
        rows = table.find_all("tr")
        return list(
            row for row in self.get_row_readable_data(rows[1:])
        )  # the first one is header

    def get_popular_websites_table_as_dataclass(self):
        rows = self._get_popular_websites_table_as_rows()
        rows_objects = [
            WikiPopularLanguagesTableRow(
                website=row[0],
                _popularity=row[1],
                frontend=row[2],
                backend=row[3],
                database=row[4],
                notes=row[5],
            )
            for row in rows
        ]
        return WikiPopularLanguagesTable(rows=rows_objects)

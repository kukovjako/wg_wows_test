import re
from dataclasses import dataclass
from typing import List

from base.config import GET_INT_PATTERN


@dataclass
class WikiPopularLanguagesTableRow:
    website: str
    _popularity: str
    frontend: str
    backend: str
    database: str
    notes: str = None

    @property
    def popularity(self) -> int:
        _str = re.sub(GET_INT_PATTERN, "", self._popularity)
        return int(_str)


@dataclass
class WikiPopularLanguagesTable:
    rows: List[WikiPopularLanguagesTableRow]

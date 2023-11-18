# may be stored in environment variables of a pipeline
from urllib.parse import urljoin

BASE_URL = "https://en.wikipedia.org/wiki/"
POPULAR_LANGUAGES_URL = urljoin(
    BASE_URL, "Programming_languages_used_in_most_popular_websites"
)
POPULAR_WEBSITES_TABLE_NAME = "Programming languages used in most popular websites*"
TABLE_CELLS_STRIPPING_PATTERN = "(\[\d+\]|\n)"
GET_INT_PATTERN = "[^0-9]"

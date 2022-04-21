from typing import List


def join_urls(urls: List[str]) -> str:
    """Join URLs.

    Join absolute and relative URLs.
    """

    return _sanitize_url("/".join(urls))


def _sanitize_url(url: str) -> str:
    """Clean extra / in URL."""

    url = url.replace("///", "/")
    url = url.replace("//", "/")
    url = url.replace("http:/", "http://")
    url = url.replace("https:/", "https://")
    url = url.replace("/http", "http")
    return url

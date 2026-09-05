"""Structural validation for the static portfolio pages.

Guards against the two failure modes a hand-edited multi-page HTML site is
prone to: a page missing basic head metadata, and an internal link that
points at a file which no longer exists.
"""

from pathlib import Path

import pytest
from bs4 import BeautifulSoup

SITE_ROOT = Path(__file__).resolve().parent.parent
HTML_PAGES = sorted(SITE_ROOT.glob("*.html"))


def _soup(path: Path) -> BeautifulSoup:
    return BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")


@pytest.mark.parametrize("page", HTML_PAGES, ids=lambda p: p.name)
def test_page_has_title(page):
    soup = _soup(page)
    title = soup.find("title")
    assert title is not None and title.get_text(strip=True), (
        f"{page.name} is missing a non-empty <title>"
    )


@pytest.mark.parametrize("page", HTML_PAGES, ids=lambda p: p.name)
def test_page_has_viewport_meta(page):
    soup = _soup(page)
    viewport = soup.find("meta", attrs={"name": "viewport"})
    assert viewport is not None, f"{page.name} is missing the responsive viewport meta tag"


@pytest.mark.parametrize("page", HTML_PAGES, ids=lambda p: p.name)
def test_page_links_stylesheet(page):
    soup = _soup(page)
    stylesheet = soup.find("link", rel="stylesheet")
    assert stylesheet is not None and stylesheet.get("href"), (
        f"{page.name} does not link a stylesheet"
    )


@pytest.mark.parametrize("page", HTML_PAGES, ids=lambda p: p.name)
def test_page_has_nav(page):
    soup = _soup(page)
    assert soup.find("nav") is not None, f"{page.name} is missing the site <nav>"


@pytest.mark.parametrize("page", HTML_PAGES, ids=lambda p: p.name)
def test_internal_links_resolve(page):
    soup = _soup(page)
    for tag in soup.find_all(["a", "link"]):
        href = tag.get("href")
        if not href or href.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = href.split("#", 1)[0]
        if not target:
            continue
        resolved = (SITE_ROOT / target).resolve()
        assert resolved.is_file(), f"{page.name} links to missing file: {href}"

"""
These tests cover TNT searches.
"""

import pytest
from playwright.sync_api import sync_playwright, expect, Page
from pages.tracking import TrackandTraceSearchPage

TRACKS = [
    'panda',
    'python'
]

@pytest.fixture(scope='session')
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        yield context
        browser.close()

@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()

@pytest.fixture
def tracking_page(page):
    return TrackandTraceSearchPage(page)

@pytest.mark.parametrize('phrase', TRACKS)
def test_basic_duckduckgo_search(phrase: str, page: Page, tracking_page: TrackandTraceSearchPage) -> None:
    # Given the DuckDuckGo home page is displayed
    tracking_page.load()

    print(f"Testing with phrase: {phrase}")

    # When the user searches for a phrase
    # tracking_page.search(phrase)

    # Then the search result query is the phrase
    # expect(tracking_page.search_input).to_have_value(phrase)

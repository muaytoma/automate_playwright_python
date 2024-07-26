"""
These tests cover TNT searches.
"""

import pytest

from pages.tracking import TrackandTraceSearchPage
from playwright.sync_api import expect, Page


TRACKS = [
  'panda',
  'python'
]

# POD have photo
# @pytest.mark.parametrize('phrase', TRACKS)
# def test_get_search_success()  -> None:
#   print()


    
@pytest.mark.parametrize('phrase', TRACKS)
def test_basic_duckduckgo_search(
    phrase: str,
    page: Page,
    tracking_page: TrackandTraceSearchPage) -> None:
    
    # Given the DuckDuckGo home page is displayed
    tracking_page.load()

    print(f"Testing with phrase: {phrase}")
        # When the user searches for a phrase
    # tracking_page.search(phrase)

    # # Then the search result query is the phrase
    # expect(tracking_page.search_input).to_have_value(phrase)
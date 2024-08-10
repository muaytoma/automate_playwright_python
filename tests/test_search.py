import pytest
from pages.search_page import SearchPage
from playwright.sync_api import expect, Page

TRACKS = [
    'python',
    'automate'
]

@pytest.mark.parametrize('phrase', TRACKS)
def test_google_search(
    phrase: str,
    page: Page,
    search_page: SearchPage) -> None:
    
    # Given the Google search page is displayed
    search_page.load()

    print(f"Testing with phrase: {phrase}")
    
    # When the user searches for the phrase
    search_page.search(phrase)

    # Then the search result page should display results for the phrase
    expect(search_page.search_input).to_have_value(phrase)

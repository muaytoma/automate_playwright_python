import pytest
from playwright.sync_api import Page, Playwright
from pages.search_page import SearchPage

@pytest.fixture(scope='function')
def page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()

@pytest.fixture(scope='function')
def search_page(page: Page) -> SearchPage:
    return SearchPage(page)

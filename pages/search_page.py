from playwright.sync_api import Page

class SearchPage:
    URL = 'https://www.google.co.th/'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_button = page.locator('input[name="btnK"]').nth(1)
        self.search_input = page.locator('textarea[name="q"]')
    
    def load(self) -> None:
        """
        Navigate to the Google search page.
        """
        self.page.goto(self.URL)
        self.page.wait_for_selector('textarea[name="q"]')

    def search(self, phrase: str) -> None:
        """
        Perform a search with the given phrase.

        Args:
            phrase (str): The search term to enter in the search input field.
        """
        self.search_input.fill(phrase)
        self.search_button.click()

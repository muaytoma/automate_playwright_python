"""
This module contains shared fixtures.
"""
# ------------------------------------------------------------
# Imports
# ------------------------------------------------------------

import os
import pytest

from pages.tracking import TrackandTraceSearchPage
from playwright.sync_api import Playwright, APIRequestContext, Page, expect
from typing import Generator

# ------------------------------------------------------------
# Track and Trace tracking fixtures
# ------------------------------------------------------------

@pytest.fixture
def tracking_page(page: Page) -> TrackandTraceSearchPage:
  return TrackandTraceSearchPage(page)


@pytest.fixture(scope='function')
def page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()
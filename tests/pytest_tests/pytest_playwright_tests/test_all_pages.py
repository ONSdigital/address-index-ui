""" Playwright tests against each page. """
from playwright.sync_api import Page

from tests.pytest_tests.pytest_playwright_tests.utils.constants import BASE_URL


def test_header_present(page: Page):
    page.goto(BASE_URL)
    assert page.get_by_role('')


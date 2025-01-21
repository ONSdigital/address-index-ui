""" Playwright tests against each page. """
import pytest
from playwright.sync_api import Page, expect
from tests.pytest_tests.pytest_playwright_tests.utils.constants import (
    ALL_PAGE_NAMES, BASE_URL, ROLES, get_just_header_pages, role_to_username)


def test_title_tag(page: Page):
  page.goto(BASE_URL)

  expect(page).to_have_title('Address Index')


def test_header_visible(page: Page):
  page.goto(BASE_URL)

  expect(page.locator('header')).to_be_visible()


@pytest.mark.parametrize("user_role", ROLES)
@pytest.mark.parametrize("page_name", ALL_PAGE_NAMES)
class TestPageElements:
  """Test various elements (header, footer, etc.) on each page for each role."""

  def test_header_is_visible_and_has_correct_links(self, page: Page,
                                                   user_role: str,
                                                   page_name: str,
                                                   login_and_goto):
    page = login_and_goto(user_role, page_name)

    # HEADER checks
    expect(page.locator('header')).to_be_visible()
    user_info_for_role = role_to_username(user_role)
    allowed_pages_info = user_info_for_role.get('allowed_pages_info')
    expected_header_pages = get_just_header_pages(allowed_pages_info)

    print(
        f'\n FOR THE USERNAME "{user_info_for_role.get("username")}",'
        f' with ROLE {user_role},'
        f' the EXPECTED HEADER PAGES are:'
        f' {[ "  name: " + x.get("page_name") + "\n    url:" + x.get("url") for x in expected_header_pages]}\n'
    )

    for allowed_page in expected_header_pages:
      link_element = page.locator('.ons-navigation__link').filter(
          has_text=allowed_page.get('page_name'))
      expected_page_uri = f"/{allowed_page.get('url')}"
      print(f'   Checking link: {allowed_page.get("page_name")}'
            f' should have url: {expected_page_uri}')
      print(
          'Check that the last tested link *should be visible* for the user role.'
      )

      expect(link_element).to_have_attribute('href', expected_page_uri)

  def test_footer_is_visible_and_correct(self, page: Page, user_role: str,
                                         page_name: str, login_and_goto):
    page = login_and_goto(user_role, page_name)

    # FOOTER checks
    footer = page.locator('footer')
    expect(footer).to_be_visible()

    footer_help_link = footer.get_by_text(
        'Have feedback or found an issue with matched address(es)?')
    expect(footer_help_link).to_have_attribute('href', '/help/submit_feedback')

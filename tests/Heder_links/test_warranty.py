import re

from playwright.sync_api import expect


def test_header_link(page_fixture):
    url = "https://garwin.ru/"
    page_fixture.goto(f'{url}', wait_until='domcontentloaded')
    page_fixture.get_by_role("banner").get_by_role("link", name="Гарантии").click()
    page_fixture.wait_for_url(f'{url}warranty')
    expect(page_fixture).to_have_url(f'{url}warranty')
    response = page_fixture.request.get(f'{url}warranty')
    expect(response).to_be_ok()
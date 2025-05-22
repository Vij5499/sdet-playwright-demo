from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.screenshot(path="google.png")
    browser.close()
# tests/test_google.py
def test_google_homepage(browser):
    page = browser.new_page()
    page.goto("https://www.google.com")
    assert "Google" in page.title()
    page.screenshot(path="google.png")
    page.close()


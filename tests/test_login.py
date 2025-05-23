# tests/test_login.py

from Pages.login_page import LoginPage

def test_valid_login(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"
    page.close()

def test_invalid_login(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("invalid_user", "wrong_password")
    error = login_page.get_error()
    assert "Username and password do not match" in error or "do not match" in error
    page.close()

def test_logout(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    # Click menu → logout
    page.locator("#react-burger-menu-btn").click()
    page.locator("#logout_sidebar_link").click()
    
    assert page.url == "https://www.saucedemo.com/"
    page.close()
def test_locked_out_user(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")
    
    error = login_page.get_error()
    assert "Sorry, this user has been locked out." in error
    page.close()

def test_problem_user_login(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("problem_user", "secret_sauce")

    # Confirm it loads, but images may be broken (simulate broken UI)
    inventory_images = page.locator(".inventory_item_img")
    assert inventory_images.count() == 12
    page.close()

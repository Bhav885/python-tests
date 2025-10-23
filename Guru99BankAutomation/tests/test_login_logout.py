# from pages.guru_login_page import GuruLoginPage
# from pages.guru_home_page import GuruHomePage
#
# def test_valid_login_logout(setup):
#     login = GuruLoginPage(setup)
#     login.open()
#     login.login("mngr640697", "vevAdEt")  # replace with working creds
#
#     home = GuruHomePage(setup)
#     assert "Manger Id" in home.get_welcome_text()
#
#     home.logout()
#     assert "Guru99 Bank" in setup.title

import pytest
from selenium import webdriver
from pages.guru_login_page import GuruLoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):  # ✅ must start with 'test_'
    login_page = GuruLoginPage(driver)
    login_page.open()
    login_page.login("mngr640697", "vevAdEt")
    assert "Guru99 Bank Manager HomePage" in driver.title



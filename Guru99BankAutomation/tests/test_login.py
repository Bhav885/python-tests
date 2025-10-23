# import pytest
# from selenium import webdriver
# from pages.guru_login_page import GuruLoginPage
#
# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#
# def test_valid_login(driver):
#     login_page = GuruLoginPage(driver)
#     login_page.open()
#     login_page.login("mngr640697", "vevAdEt")  # replace with valid credentials
#
#     # Check if login error is NOT displayed
#     assert not login_page.is_login_error_displayed()

import pytest
from selenium import webdriver
from pages.guru_login_page import GuruLoginPage
def test_valid_login(setup):
    login_page = GuruLoginPage(setup)
    login_page.open()
    login_page.login("mngr640697", "vevAdEt")  # replace with valid credentials
    # Check if login error is NOT displayed
    assert not login_page.is_login_error_displayed()









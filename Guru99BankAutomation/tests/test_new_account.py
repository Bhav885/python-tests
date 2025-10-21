import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.guru_login_page import GuruLoginPage
from pages.guru_home_page import GuruHomePage
from pages.guru_new_account_page import GuruNewAccountPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_create_new_account(driver):
    # Step 1: Login
    login_page = GuruLoginPage(driver)
    login_page.open()
    login_page.login("mngr640697", "vevAdEt")  # use valid credentials

    # Step 2: Verify login
    home_page = GuruHomePage(driver)
    assert "Manger Id" in home_page.get_welcome_text()

    # Step 3: Open New Account page and create account for existing customer
    new_account_page = GuruNewAccountPage(driver)
    new_account_page.open_new_account_form()

    # Use existing Customer ID
    customer_id = "66453"  # replace with a valid existing Customer ID
    new_account_page.create_account(customer_id, "Savings", "1000")

    # Step 4: Verify account creation
    assert new_account_page.is_account_created()

    # Step 5: Logout
    home_page.logout()

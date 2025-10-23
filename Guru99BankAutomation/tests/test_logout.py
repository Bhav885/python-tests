import pytest
from pages.guru_login_page import GuruLoginPage
from pages.guru_home_page import GuruHomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_logout(setup):
    """Test logout functionality using global setup fixture"""
    driver = setup

    # Login first
    login_page = GuruLoginPage(driver)
    login_page.open()
    login_page.login("mngr640697", "vevAdEt")  # valid credentials

    # Home page actions
    home_page = GuruHomePage(driver)
    welcome_text = home_page.get_welcome_text()
    assert "Manger Id" in welcome_text  # verify login successful

    # Logout
    home_page.logout()

    # Verify back on login page
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(EC.visibility_of_element_located((By.NAME, "btnLogin")))
    assert login_button.is_displayed()


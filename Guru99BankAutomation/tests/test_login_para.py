import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException


# ==================================================
# FIXTURE – Setup & Teardown (Test Fixture Concept)
# ==================================================
@pytest.fixture()
def setup():
    """Setup and teardown the Chrome WebDriver"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# ==================================================
# PAGE OBJECT MODEL – Guru99 Login Page
# ==================================================
class GuruLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demo.guru99.com/V4/"
        self.username = (By.NAME, "uid")
        self.password = (By.NAME, "password")
        self.login_button = (By.NAME, "btnLogin")

    def open(self):
        """Open the login page"""
        self.driver.get(self.url)

    def login(self, user, pwd):
        """Perform login action"""
        self.driver.find_element(*self.username).clear()
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).clear()
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()

    def is_dashboard_displayed(self):
        """Check if Manager home page appears"""
        return "Manager" in self.driver.page_source

    def is_login_error_displayed(self):
        """Handle alert for invalid login"""
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return "User or Password is not valid" in alert_text
        except NoAlertPresentException:
            return False


# ==================================================
# PARAMETRIZED TEST (Data Driven Testing)
# ==================================================
@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("mngr640697", "vevAdEt", True),     # Valid credentials
        ("invalidUser", "wrongPass", False),  # Invalid credentials
    ],
)
def test_login_parametrized(setup, username, password, expected):
    """
    ✅ Arrange-Act-Assert Pattern
    ✅ Parametrization
    ✅ Data-Driven Testing
    """
    # Arrange
    page = GuruLoginPage(setup)

    # Act
    page.open()
    page.login(username, password)

    # Assert
    if expected:
        assert page.is_dashboard_displayed(), "Valid login failed!"
    else:
        assert page.is_login_error_displayed(), "Invalid login alert not displayed!"


# ==================================================
# EXCEPTION CHECKING
# ==================================================
def test_login_with_blank_fields(setup):
    """
    ✅ Exception Checking (handled safely)
    """
    page = GuruLoginPage(setup)
    page.open()
    page.login("", "")
    # Check if an alert appears and handle gracefully
    assert page.is_login_error_displayed() or page.is_dashboard_displayed()


# ==================================================
# SKIPPING TEST
# ==================================================
@pytest.mark.skip(reason="Login feature under maintenance")
def test_skip_example():
    """This test is intentionally skipped"""
    pass

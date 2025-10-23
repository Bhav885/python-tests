import pytest
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ==================================================
# PAGE OBJECT MODEL – Guru99 Login Page
# ==================================================
class GuruLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demo.guru99.com/V4/"
        self.username_locator = (By.NAME, "uid")
        self.password_locator = (By.NAME, "password")
        self.login_button_locator = (By.NAME, "btnLogin")
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Open the login page"""
        self.driver.get(self.url)
        # Wait for page to load
        self.wait.until(EC.presence_of_element_located(self.login_button_locator))

    def login(self, user, pwd):
        """Perform login action"""
        username_field = self.wait.until(EC.presence_of_element_located(self.username_locator))
        password_field = self.driver.find_element(*self.password_locator)
        login_btn = self.driver.find_element(*self.login_button_locator)

        username_field.clear()
        username_field.send_keys(user)
        password_field.clear()
        password_field.send_keys(pwd)
        login_btn.click()

    def is_dashboard_displayed(self):
        """Check if Manager home page appears"""
        try:
            # Wait a moment for page transition
            time.sleep(1)

            # Get page source safely
            page_source = self.driver.page_source

            # Check if page_source is valid
            if not page_source:
                return False

            # Check for Manager dashboard indicators
            return "Manager" in page_source or "Manger Id" in page_source

        except Exception as e:
            print(f"Error checking dashboard: {e}")
            return False

    def is_login_error_displayed(self):
        """Handle alert for invalid login"""
        try:
            # Wait for alert to be present
            alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert_text = alert.text
            print(f"Alert text: {alert_text}")
            alert.accept()

            # Wait a bit after accepting alert
            time.sleep(0.5)

            # Check for common error messages
            error_messages = [
                "User or Password is not valid",
                "User-ID must not be blank",
                "Password must not be blank"
            ]

            return any(msg in alert_text for msg in error_messages)

        except TimeoutException:
            print("No alert found")
            return False
        except NoAlertPresentException:
            print("Alert not present")
            return False
        except Exception as e:
            print(f"Error handling alert: {e}")
            return False

    def is_on_login_page(self):
        """Check if still on login page"""
        try:
            time.sleep(0.5)
            return self.driver.find_element(*self.login_button_locator).is_displayed()
        except Exception:
            return False


# ==================================================
# PARAMETRIZED TEST (Data Driven Testing)
# ==================================================
@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("mngr640697", "vevAdEt", True),  # Valid credentials
        ("invalidUser", "wrongPass", False),  # Invalid credentials
    ],
)
def test_login_parametrized(setup, username, password, expected):
    """
    ✅ Arrange-Act-Assert Pattern
    ✅ Parametrization
    ✅ Data-Driven Testing
    """
    # Arrange - Use global setup fixture
    driver = setup
    page = GuruLoginPage(driver)

    # Act
    page.open()
    page.login(username, password)

    # Assert
    if expected:
        assert page.is_dashboard_displayed(), "Valid login failed!"
    else:
        error_displayed = page.is_login_error_displayed()
        assert error_displayed, "Invalid login alert not displayed!"


# ==================================================
# EXCEPTION CHECKING
# ==================================================
def test_login_with_blank_fields(setup):
    """
    ✅ Exception Checking (handled safely)
    """
    driver = setup
    page = GuruLoginPage(driver)

    # Arrange & Act
    page.open()
    page.login("", "")

    # Assert - Either alert appears OR we stay on login page
    # (behavior may vary, so we check both possibilities)
    alert_appeared = page.is_login_error_displayed()
    on_login_page = page.is_on_login_page()
    not_on_dashboard = not page.is_dashboard_displayed()

    # At least one should be true
    assert alert_appeared or (on_login_page and not_on_dashboard), \
        "Expected alert or to remain on login page when submitting blank fields"


# ==================================================
# SKIPPING TEST
# ==================================================
@pytest.mark.skip(reason="Login feature under maintenance")
def test_skip_example():
    """This test is intentionally skipped"""
    pass
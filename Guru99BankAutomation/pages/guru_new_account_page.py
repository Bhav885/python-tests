from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GuruNewAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # Locators
        self.new_account_link = (By.LINK_TEXT, "New Account")
        self.customer_id_input = (By.NAME, "cusid")
        self.account_type_dropdown = (By.NAME, "selaccount")
        self.initial_deposit_input = (By.NAME, "inideposit")
        self.submit_button = (By.NAME, "button2")
        self.success_message = (By.XPATH, "//p[contains(text(), 'Account Generated Successfully')]")

    def open_new_account_form(self):
        self.wait.until(EC.element_to_be_clickable(self.new_account_link)).click()

    def create_account(self, customer_id, account_type="Savings", initial_deposit="500"):
        # Fill Customer ID
        self.wait.until(EC.visibility_of_element_located(self.customer_id_input)).send_keys(customer_id)

        # Select account type
        dropdown = self.driver.find_element(*self.account_type_dropdown)
        for option in dropdown.find_elements(By.TAG_NAME, "option"):
            if option.text.strip() == account_type:
                option.click()
                break

        # Fill initial deposit
        self.driver.find_element(*self.initial_deposit_input).send_keys(initial_deposit)
        self.driver.find_element(*self.submit_button).click()

    def is_account_created(self):
        """Return True if success message appears"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.success_message))
            return element.is_displayed()
        except:
            return False

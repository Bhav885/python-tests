# pages/guru_new_customer_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class GuruNewCustomerPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_new_customer_page(self):
        """Click 'New Customer' link from home page"""
        new_customer_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "New Customer"))
        )
        new_customer_link.click()

    def add_new_customer(self, name, gender, dob, address, city, state, pin, mobile, email, password):
        """
        Fill and submit the New Customer form.
        Expected DOB format: dd/mm/yyyy (e.g., "01/01/1990")
        """
        wait = self.wait

        # Name
        wait.until(EC.visibility_of_element_located((By.NAME, "name"))).send_keys(name)

        # Gender (m or f)
        gender_radio = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//input[@value='{gender}']"))
        )
        gender_radio.click()

        # Date of Birth (dd/mm/yyyy)
        wait.until(EC.visibility_of_element_located((By.NAME, "dob"))).send_keys(dob)

        # Address
        wait.until(EC.visibility_of_element_located((By.NAME, "addr"))).send_keys(address)

        # City
        wait.until(EC.visibility_of_element_located((By.NAME, "city"))).send_keys(city)

        # State
        wait.until(EC.visibility_of_element_located((By.NAME, "state"))).send_keys(state)

        # PIN (6 digits)
        wait.until(EC.visibility_of_element_located((By.NAME, "pinno"))).send_keys(pin)

        # Mobile Number (10 digits)
        wait.until(EC.visibility_of_element_located((By.NAME, "telephoneno"))).send_keys(mobile)

        # Email
        wait.until(EC.visibility_of_element_located((By.NAME, "emailid"))).send_keys(email)

        # Password
        wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys(password)

        # Submit
        submit_btn = wait.until(EC.element_to_be_clickable((By.NAME, "sub")))
        submit_btn.click()

    def get_customer_id(self):
        """Extract Customer ID from success page"""
        try:
            cust_id_element = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//td[text()='Customer ID']/following-sibling::td")
                )
            )
            return cust_id_element.text.strip()
        except TimeoutException:
            return None
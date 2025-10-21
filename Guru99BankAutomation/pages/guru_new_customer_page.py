from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GuruNewCustomerPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 12)

    def open_new_customer_page(self):
        link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "New Customer")))
        link.click()

    def add_new_customer(self, name, gender, dob, address, city, state, pin, mobile, email, password):
        self.wait.until(EC.visibility_of_element_located((By.NAME, "name"))).send_keys(name)
        self.driver.find_element(By.XPATH, f"//input[@value='{gender}']").click()
        self.driver.find_element(By.NAME, "dob").send_keys(dob)
        self.driver.find_element(By.NAME, "addr").send_keys(address)
        self.driver.find_element(By.NAME, "city").send_keys(city)
        self.driver.find_element(By.NAME, "state").send_keys(state)
        self.driver.find_element(By.NAME, "pinno").send_keys(pin)
        self.driver.find_element(By.NAME, "telephoneno").send_keys(mobile)
        self.driver.find_element(By.NAME, "emailid").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.NAME, "sub").click()

    def get_customer_id(self):
        return self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//td[text()='Customer ID']/following-sibling::td")
        )).text

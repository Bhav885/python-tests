# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class GuruHomePage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 12)
#
#     def get_welcome_text(self):
#         return self.wait.until(EC.visibility_of_element_located(
#             (By.XPATH, "//td[contains(text(),'Manger Id')]")
#         )).text
#
#     def logout(self):
#         logout_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log out")))
#         logout_link.click()
#         alert = self.driver.switch_to.alert
#         alert.accept()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class GuruHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.logout_link = (By.LINK_TEXT, "Log out")

    def get_welcome_text(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Manger Id')]"))
        )
        return element.text

    def logout(self):
        wait = WebDriverWait(self.driver, 10)
        logout_link = wait.until(EC.element_to_be_clickable(self.logout_link))
        time.sleep(2)  # small buffer for overlapping elements
        self.driver.execute_script("arguments[0].scrollIntoView(true);", logout_link)
        self.driver.execute_script("arguments[0].click();", logout_link)

        # Handle alert popup
        alert = wait.until(EC.alert_is_present())
        alert.accept()


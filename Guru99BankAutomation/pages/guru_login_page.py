# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class GuruLoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 12)
#
#     def open(self):
#         self.driver.get("http://demo.guru99.com/V4/")
#
#     def login(self, userid, password):
#         user = self.wait.until(EC.visibility_of_element_located((By.NAME, "uid")))
#         pwd = self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
#         login_btn = self.wait.until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
#
#         user.clear()
#         user.send_keys(userid)
#         pwd.clear()
#         pwd.send_keys(password)
#         login_btn.click()
#
#     def is_login_error_displayed(self):
#         try:
#             return self.driver.find_element(By.XPATH, "//p[@class='error']").is_displayed()
#         except:
#             return False

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GuruLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://demo.guru99.com/V4/"  # your login page URL

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(By.NAME, "uid").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.NAME, "btnLogin").click()

    def is_login_successful(self):
        try:
            # Wait for manager home page welcome text
            element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//td[contains(text(),'Manger Id')]"))
            )
            return True
        except:
            return False

    def is_login_failed(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return "User or Password is not valid" in alert_text
        except:
            return False

    def is_login_error_displayed(self):
        try:
            return self.driver.find_element(By.XPATH, "//p[@class='error']").is_displayed()
        except:
            return False


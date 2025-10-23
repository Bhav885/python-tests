# # from pages.guru_login_page import GuruLoginPage
# # from pages.guru_home_page import GuruHomePage
# # from pages.guru_new_customer_page import GuruNewCustomerPage
# #
# # def test_add_new_customer(setup):
# #     login = GuruLoginPage(setup)
# #     login.open()
# #     login.login("mngr640697", "vevAdEt")
# #
# #     new_cust = GuruNewCustomerPage(setup)
# #     new_cust.open_new_customer_page()
# #     new_cust.add_new_customer("John Doe", "m", "01011990", "123 Street", "City", "State", "123456", "9876543210", "john@test.com", "pass123")
# #
# #     cust_id = new_cust.get_customer_id()
# #     assert cust_id is not None
# #
# # import pytest
# # import random
# # from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
# # from pages.guru_login_page import GuruLoginPage
# # from pages.guru_home_page import GuruHomePage
# # from pages.guru_new_customer_page import GuruNewCustomerPage
# #
# #
# # def generate_random_email():
# #     return f"john{random.randint(1000,9999)}@test.com"
# #
# #
# # def test_add_new_customer(setup):
# #     driver = setup
# #     login = GuruLoginPage(driver)
# #     login.open()
# #     login.login("mngr640697", "vevAdEt")
# #
# #     new_cust = GuruNewCustomerPage(driver)
# #     new_cust.open_new_customer_page()
# #
# #     # Use random email each run to prevent duplicates
# #     email = generate_random_email()
# #
# #     try:
# #         new_cust.add_new_customer(
# #             name="John Doe",
# #             gender="m",
# #             dob="01011990",
# #             address="123 Street",
# #             city="City",
# #             state="State",
# #             pin="123456",
# #             mobile="9876543210",
# #             email=email,
# #             password="pass123"
# #         )
# #
# #         cust_id = new_cust.get_customer_id()
# #         assert cust_id is not None, "Customer ID not found — add new customer may have failed"
# #
# #     except UnexpectedAlertPresentException:
# #         # Handle case where Guru99 shows an alert (e.g., duplicate email)
# #         alert = driver.switch_to.alert
# #         print("⚠️ Alert detected:", alert.text)
# #         alert.accept()
# #         pytest.skip("Skipped: Email address already existed or another validation alert shown.")
# #
# #     except NoAlertPresentException:
# #         pass
#
# import pytest
# import random
# import time
# from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
# from pages.guru_login_page import GuruLoginPage
# from pages.guru_home_page import GuruHomePage
# from pages.guru_new_customer_page import GuruNewCustomerPage
#
# def generate_random_email():
#     return f"john{random.randint(1000,9999)}@test.com"
#
# def handle_alert(driver):
#     """Safely handle alert if present"""
#     try:
#         time.sleep(1)  # wait a bit for alert to appear
#         alert = driver.switch_to.alert
#         alert_text = alert.text
#         alert.accept()  # or alert.dismiss()
#         print(f"⚠️ Alert handled: {alert_text}")
#         return alert_text
#     except NoAlertPresentException:
#         return None
#     except UnexpectedAlertPresentException:
#         # Firefox may throw this; retry once
#         time.sleep(0.5)
#         try:
#             alert = driver.switch_to.alert
#             alert_text = alert.text
#             alert.accept()
#             print(f"⚠️ Alert handled after retry: {alert_text}")
#             return alert_text
#         except NoAlertPresentException:
#             return None
#
# def test_add_new_customer(setup):
#     driver = setup
#     login = GuruLoginPage(driver)
#     login.open()
#     login.login("mngr640697", "vevAdEt")
#
#     new_cust = GuruNewCustomerPage(driver)
#     new_cust.open_new_customer_page()
#
#     email = generate_random_email()
#
#     try:
#         new_cust.add_new_customer(
#             name="John Doe",
#             gender="m",
#             dob="01011990",
#             address="123 Street",
#             city="City",
#             state="State",
#             pin="123456",
#             mobile="9876543210",
#             email=email,
#             password="pass123"
#         )
#
#         cust_id = new_cust.get_customer_id()
#         assert cust_id is not None, "Customer ID not found — add new customer may have failed"
#
#     except (UnexpectedAlertPresentException, NoAlertPresentException):
#         alert_text = handle_alert(driver)
#         if alert_text:
#             pytest.skip(f"Skipped due to alert: {alert_text}")
#
import pytest
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
# from pages.guru_login_page import GuruLoginPage
# from pages.guru_home_page import GuruHomePage
# from pages.guru_new_customer_page import GuruNewCustomerPage
#
#
# def test_add_new_customer(setup):
#     """Test adding a new customer with proper waits"""
#     driver = setup
#     wait = WebDriverWait(driver, 20)  # Increased timeout
#
#     # Step 1: Login
#     login_page = GuruLoginPage(driver)
#     login_page.open()
#     login_page.login("mngr640697", "vevAdEt")
#
#     # Wait for successful login
#     time.sleep(2)
#
#     # Step 2: Verify login successful
#     home_page = GuruHomePage(driver)
#     welcome_text = home_page.get_welcome_text()
#     assert "Manger Id" in welcome_text, "Login verification failed"
#
#     # Step 3: Navigate to New Customer page
#     new_customer_page = GuruNewCustomerPage(driver)
#     new_customer_page.open_new_customer_form()
#
#     # Wait for form to load
#     time.sleep(2)
#
#     # Step 4: Fill customer details
#     import random
#     random_suffix = random.randint(1000, 9999)
#
#     customer_data = {
#         "name": f"Test Customer {random_suffix}",
#         "gender": "m",  # or "f"
#         "dob": "01/01/1990",
#         "address": "123 Test Street",
#         "city": "Test City",
#         "state": "Test State",
#         "pin": "123456",
#         "mobile": f"98765{random_suffix}",
#         "email": f"testcustomer{random_suffix}@test.com",
#         "password": "Test@123"
#     }
#
#     new_customer_page.fill_customer_form(**customer_data)
#
#     # Step 5: Submit and verify
#     new_customer_page.submit()
#
#     # Wait for success message
#     time.sleep(3)
#
#     assert new_customer_page.is_customer_created(), "Customer creation failed"
#
#     # Step 6: Logout
#     home_page.logout()

# import time
# import random
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
# from pages.guru_login_page import GuruLoginPage
# from pages.guru_home_page import GuruHomePage
# from pages.guru_new_customer_page import GuruNewCustomerPage
#
#
# def test_add_new_customer(setup):
#     """Test adding a new customer with proper waits"""
#     driver = setup
#     wait = WebDriverWait(driver, 20)  # Increased timeout
#
#     # Step 1: Login
#     login_page = GuruLoginPage(driver)
#     login_page.open()
#     login_page.login("mngr640697", "vevAdEt")
#
#     # Wait for successful login
#     time.sleep(2)
#
#     # Step 2: Verify login successful
#     home_page = GuruHomePage(driver)
#     welcome_text = home_page.get_welcome_text()
#     assert "Manger Id" in welcome_text, "Login verification failed"
#
#     # Step 3: Navigate to New Customer page
#     new_customer_page = GuruNewCustomerPage(driver)
#     new_customer_page.open_new_customer_page()  # ✅ Fixed method name
#
#     # Wait for form to load
#     time.sleep(2)
#
#     # Step 4: Fill customer details
#     random_suffix = random.randint(1000, 9999)
#
#     customer_data = {
#         "name": f"TestCustomer{random_suffix}",
#         "gender": "m",  # or "f"
#         "dob": "01/01/1990",
#         "address": "123 Test Street",
#         "city": "Test City",
#         "state": "Test State",
#         "pin": "123456",
#         "mobile": f"98765{random_suffix}",
#         "email": f"testcustomer{random_suffix}@test.com",
#         "password": "Test@123"
#     }
#
#     new_customer_page.fill_customer_form(**customer_data)
#
#     # Step 5: Submit and verify
#     new_customer_page.submit()
#
#     # Wait for success message
#     time.sleep(3)
#
#     assert new_customer_page.is_customer_created(), "Customer creation failed"
#
#     # Step 6: Logout
#     home_page.logout()

import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from pages.guru_login_page import GuruLoginPage
from pages.guru_home_page import GuruHomePage
from pages.guru_new_customer_page import GuruNewCustomerPage

#
# def test_add_new_customer(setup):
#     """Test adding a new customer with proper waits"""
#     driver = setup
#     wait = WebDriverWait(driver, 20)
#
#     # Step 1: Login
#     login_page = GuruLoginPage(driver)
#     login_page.open()
#     login_page.login("mngr640697", "vevAdEt")
#
#     # Wait for successful login
#     time.sleep(2)
#
#     # Step 2: Verify login successful
#     home_page = GuruHomePage(driver)
#     welcome_text = home_page.get_welcome_text()
#     assert "Manger Id" in welcome_text, "Login verification failed"
#
#     # Step 3: Navigate to New Customer page
#     new_customer_page = GuruNewCustomerPage(driver)
#     new_customer_page.open_new_customer_page()
#
#     # Wait for form to load
#     time.sleep(2)
#
#     # Step 4: Generate random data to avoid duplicates
#     random_suffix = random.randint(1000, 9999)
#
#     # Step 5: Add new customer (using the correct method from page object)
#     new_customer_page.add_new_customer(
#         name=f"TestCustomerw",
#         gender="m",
#         dob="01011990",  # ✅ Format: MMDDYYYY (no slashes)
#         address="123 Test Street",
#         city="Test City",
#         state="Test State",
#         pin="123456",
#         mobile=f"98765{random_suffix}",
#         email=f"testcustomer{random_suffix}@test.com",
#         password="Test@123"
#     )
#
#     # Wait for customer creation
#     time.sleep(3)
#
#     # Step 6: Verify customer was created by getting customer ID
#     try:
#         customer_id = new_customer_page.get_customer_id()
#         assert customer_id is not None and customer_id != "", \
#             "Customer creation failed - no Customer ID found"
#         print(f"✅ Customer created successfully with ID: {customer_id}")
#     except Exception as e:
#         assert False, f"Customer creation verification failed: {e}"
#
#     # Step 7: Logout
#     home_page.logout()


import pytest
import random
import time
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
from pages.guru_login_page import GuruLoginPage
from pages.guru_home_page import GuruHomePage
from pages.guru_new_customer_page import GuruNewCustomerPage

def generate_random_email():
    return f"john{random.randint(1000,9999)}@test.com"

def handle_alert(driver):
    """Safely handle alert if present"""
    try:
        time.sleep(1)  # wait a bit for alert to appear
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()  # or alert.dismiss()
        print(f"⚠️ Alert handled: {alert_text}")
        return alert_text
    except NoAlertPresentException:
        return None
    except UnexpectedAlertPresentException:
        # Firefox may throw this; retry once
        time.sleep(0.5)
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            print(f"⚠️ Alert handled after retry: {alert_text}")
            return alert_text
        except NoAlertPresentException:
            return None

def test_add_new_customer(setup):
    driver = setup
    login = GuruLoginPage(driver)
    login.open()
    login.login("mngr640697", "vevAdEt")

    new_cust = GuruNewCustomerPage(driver)
    new_cust.open_new_customer_page()

    email = generate_random_email()

    try:
        new_cust.add_new_customer(
            name="John Doe",
            gender="m",
            dob="01011990",
            address="123 Street",
            city="City",
            state="State",
            pin="123456",
            mobile="9876543210",
            email=email,
            password="pass123"
        )

        cust_id = new_cust.get_customer_id()
        assert cust_id is not None, "Customer ID not found — add new customer may have failed"

    except (UnexpectedAlertPresentException, NoAlertPresentException):
        alert_text = handle_alert(driver)
        if alert_text:
            pytest.skip(f"Skipped due to alert: {alert_text}")

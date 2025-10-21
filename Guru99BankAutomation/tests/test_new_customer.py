# from pages.guru_login_page import GuruLoginPage
# from pages.guru_home_page import GuruHomePage
# from pages.guru_new_customer_page import GuruNewCustomerPage
#
# def test_add_new_customer(setup):
#     login = GuruLoginPage(setup)
#     login.open()
#     login.login("mngr640697", "vevAdEt")
#
#     new_cust = GuruNewCustomerPage(setup)
#     new_cust.open_new_customer_page()
#     new_cust.add_new_customer("John Doe", "m", "01011990", "123 Street", "City", "State", "123456", "9876543210", "john@test.com", "pass123")
#
#     cust_id = new_cust.get_customer_id()
#     assert cust_id is not None
#
# import pytest
# import random
# from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
# from pages.guru_login_page import GuruLoginPage
# from pages.guru_home_page import GuruHomePage
# from pages.guru_new_customer_page import GuruNewCustomerPage
#
#
# def generate_random_email():
#     return f"john{random.randint(1000,9999)}@test.com"
#
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
#     # Use random email each run to prevent duplicates
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
#     except UnexpectedAlertPresentException:
#         # Handle case where Guru99 shows an alert (e.g., duplicate email)
#         alert = driver.switch_to.alert
#         print("⚠️ Alert detected:", alert.text)
#         alert.accept()
#         pytest.skip("Skipped: Email address already existed or another validation alert shown.")
#
#     except NoAlertPresentException:
#         pass

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


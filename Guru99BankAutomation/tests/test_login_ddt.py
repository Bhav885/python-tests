# # import pandas as pd
# # import pytest
# # from pages.guru_login_page import GuruLoginPage
# # from pages.guru_home_page import GuruHomePage
# #
# # # Read test data from CSV
# # data = pd.read_csv("Guru99BankAutomation/test_data.csv")
# #
# # @pytest.mark.parametrize("username,password", data.values.tolist())
# # def test_login_with_csv(setup, username, password):
# #     driver = setup
# #     login = GuruLoginPage(driver)
# #     login.open()
# #     login.login(username, password)
# #
# #     # Verification logic
# #     if username == "mngr640697" and password == "vevAdEt":
# #         # Expected to log in successfully
# #         home = GuruHomePage(driver)
# #         assert "Manger Id" in home.get_welcome_text(), "Login failed for valid credentials"
# #     else:
# #         # Expected to show error alert
# #         alert = driver.switch_to.alert
# #         assert "User or Password is not valid" in alert.text
# #         alert.accept()
#
# import pandas as pd
# import pytest
# from pages.guru_login_page import GuruLoginPage
#
# data = pd.read_csv("Guru99BankAutomation/test_data.csv")
# browsers = ["chrome", "firefox"]
#
# @pytest.mark.parametrize("username,password", data.values.tolist())
# def test_login_with_csv(setup, username, password):
#     login = GuruLoginPage(setup)
#     login.open()
#     login.login(username, password)
#
#     if username.startswith("mngr"):  # valid users (like your real manager ID)
#         assert login.is_login_successful(), f"Login failed for valid user: {username}"
#     else:
#         assert login.is_login_failed(), f"Invalid login did not show alert for: {username}"



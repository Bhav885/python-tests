from pages.guru_login_page import GuruLoginPage
from pages.guru_home_page import GuruHomePage

def test_valid_login_logout(setup):
    login = GuruLoginPage(setup)
    login.open()
    login.login("mngr640697", "vevAdEt")  # replace with working creds

    home = GuruHomePage(setup)
    assert "Manger Id" in home.get_welcome_text()

    home.logout()
    assert "Guru99 Bank" in setup.title
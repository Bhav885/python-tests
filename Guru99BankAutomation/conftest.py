# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
#
# @pytest.fixture(scope="function")
# def setup():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#
# import pytest
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.firefox.service import Service as GeckoService
# from webdriver_manager.firefox import GeckoDriverManager
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="browser to run tests")
#
# @pytest.fixture(scope="function")
# def setup(request):
#     browser = request.config.getoption("--browser")
#     if browser == "chrome":
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     elif browser == "firefox":
#         driver = webdriver.Firefox(service=GeckoService(GeckoDriverManager().install()))
#     else:
#         raise ValueError(f"Unsupported browser: {browser}")
#
#     driver.maximize_window()
#     yield driver
#     driver.quit()

# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.firefox.service import Service as GeckoService
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests: chrome, firefox, edge")
#
#
# @pytest.fixture(scope="function")
# def setup(request):
#     browser = request.config.getoption("--browser").lower()
#
#     if browser == "chrome":
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     elif browser == "firefox":
#         driver = webdriver.Firefox(service=GeckoService(GeckoDriverManager().install()))
#     elif browser == "edge":
#         driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#     else:
#         raise ValueError(f"Unsupported browser: {browser}")
#
#     driver.maximize_window()
#     yield driver
#     driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# List of browsers you want to test
browsers = ["chrome", "firefox"]

@pytest.fixture(params=browsers, scope="function")
def setup(request):
    browser = request.param
    print(f"\nLaunching {browser} browser...")

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=GeckoService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()





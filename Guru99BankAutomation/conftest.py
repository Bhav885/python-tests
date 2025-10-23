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
#(working code)
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
#right one
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


# import os
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as GeckoService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#
# # Check if running in CI environment
# IS_CI = os.getenv('CI', 'false').lower() == 'true'
#
# # List of browsers you want to test
# # In CI, only use Chrome to avoid complexity and speed up tests
# browsers = ["chrome"] if IS_CI else ["chrome", "firefox"]
#
#
# @pytest.fixture(params=browsers, scope="function")
# def setup(request):
#     browser = request.param
#     print(f"\nLaunching {browser} browser...")
#
#     if browser == "chrome":
#         chrome_options = ChromeOptions()
#
#         if IS_CI:
#             # CI-specific options for Chrome
#             chrome_options.add_argument("--headless")
#             chrome_options.add_argument("--no-sandbox")
#             chrome_options.add_argument("--disable-dev-shm-usage")
#             chrome_options.add_argument("--disable-gpu")
#             chrome_options.add_argument("--window-size=1920,1080")
#             chrome_options.add_argument("--disable-extensions")
#             chrome_options.add_argument("--disable-setuid-sandbox")
#             # Prevent user data directory conflicts
#             import tempfile
#             temp_dir = tempfile.mkdtemp()
#             chrome_options.add_argument(f"--user-data-dir={temp_dir}")
#
#         driver = webdriver.Chrome(
#             service=ChromeService(ChromeDriverManager().install()),
#             options=chrome_options
#         )
#
#     elif browser == "firefox":
#         firefox_options = FirefoxOptions()
#
#         if IS_CI:
#             # CI-specific options for Firefox
#             firefox_options.add_argument("--headless")
#             firefox_options.add_argument("--width=1920")
#             firefox_options.add_argument("--height=1080")
#
#         driver = webdriver.Firefox(
#             service=GeckoService(GeckoDriverManager().install()),
#             options=firefox_options
#         )
#     else:
#         raise ValueError(f"Unsupported browser: {browser}")
#
#     driver.maximize_window()
#     yield driver
#     driver.quit()

# import os
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as GeckoService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#
# # Check if running in CI environment
# IS_CI = os.getenv('CI', 'false').lower() == 'true'
#
# # List of browsers you want to test
# # In CI, only use Chrome to avoid complexity and speed up tests
# browsers = ["chrome"] if IS_CI else ["chrome", "firefox"]
#
#
# @pytest.fixture(params=browsers, scope="function")
# def setup(request):
#     browser = request.param
#     print(f"\nLaunching {browser} browser...")
#
#     if browser == "chrome":
#         chrome_options = ChromeOptions()
#
#         if IS_CI:
#             # CI-specific options for Chrome
#             chrome_options.add_argument("--headless")
#             chrome_options.add_argument("--no-sandbox")
#             chrome_options.add_argument("--disable-dev-shm-usage")
#             chrome_options.add_argument("--disable-gpu")
#             chrome_options.add_argument("--window-size=1920,1080")
#             chrome_options.add_argument("--disable-extensions")
#             chrome_options.add_argument("--disable-setuid-sandbox")
#             # Prevent user data directory conflicts
#             import tempfile
#             temp_dir = tempfile.mkdtemp()
#             chrome_options.add_argument(f"--user-data-dir={temp_dir}")
#
#         driver = webdriver.Chrome(
#             service=ChromeService(ChromeDriverManager().install()),
#             options=chrome_options
#         )
#
#     elif browser == "firefox":
#         firefox_options = FirefoxOptions()
#
#         if IS_CI:
#             # CI-specific options for Firefox
#             firefox_options.add_argument("--headless")
#             firefox_options.add_argument("--width=1920")
#             firefox_options.add_argument("--height=1080")
#
#         driver = webdriver.Firefox(
#             service=GeckoService(GeckoDriverManager().install()),
#             options=firefox_options
#         )
#     else:
#         raise ValueError(f"Unsupported browser: {browser}")
#
#     driver.maximize_window()
#     yield driver
#     driver.quit()

# import os
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as GeckoService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
#
# # Check if running in CI environment
# IS_CI = os.getenv('CI', 'false').lower() == 'true'
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser",
#         action="store",
#         default="chrome",
#         help="Browser to run tests: chrome or firefox"
#     )
#
#
# @pytest.fixture(scope="function")
# def setup(request):
#     # Get browser from command line or environment variable
#     browser = request.config.getoption("--browser") or os.getenv('BROWSER', 'chrome')
#     browser = browser.lower()
#
#     print(f"\nLaunching {browser} browser...")
#
#     if browser == "chrome":
#         chrome_options = ChromeOptions()
#
#         if IS_CI:
#             # CI-specific options for Chrome
#             chrome_options.add_argument("--headless")
#             chrome_options.add_argument("--no-sandbox")
#             chrome_options.add_argument("--disable-dev-shm-usage")
#             chrome_options.add_argument("--disable-gpu")
#             chrome_options.add_argument("--window-size=1920,1080")
#             chrome_options.add_argument("--disable-extensions")
#             chrome_options.add_argument("--disable-setuid-sandbox")
#             import tempfile
#             temp_dir = tempfile.mkdtemp()
#             chrome_options.add_argument(f"--user-data-dir={temp_dir}")
#
#         driver = webdriver.Chrome(
#             service=ChromeService(ChromeDriverManager().install()),
#             options=chrome_options
#         )
#
#     elif browser == "firefox":
#         firefox_options = FirefoxOptions()
#
#         if IS_CI:
#             # CI-specific options for Firefox
#             firefox_options.add_argument("--headless")
#             firefox_options.add_argument("--width=1920")
#             firefox_options.add_argument("--height=1080")
#
#         driver = webdriver.Firefox(
#             service=GeckoService(GeckoDriverManager().install()),
#             options=firefox_options
#         )
#     else:
#         raise ValueError(f"Unsupported browser: {browser}")
#
#     if not IS_CI:
#         driver.maximize_window()
#
#     yield driver
#     driver.quit()
#
# import os
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as GeckoService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
#
# # Check if running in CI environment
# IS_CI = os.getenv('CI', 'false').lower() == 'true'
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser",
#         action="store",
#         default="chrome",
#         help="Browser to run tests: chrome or firefox"
#     )
#
#
# @pytest.fixture(scope="function")
# def setup(request):
#     """Global setup fixture for all tests - CI and local compatible"""
#     browser = request.config.getoption("--browser") or os.getenv('BROWSER', 'chrome')
#     browser = browser.lower()
#
#     print(f"\nLaunching {browser} browser (CI={IS_CI})...")
#
#     if browser == "chrome":
#         chrome_options = ChromeOptions()
#
#         if IS_CI:
#             # CI-specific options for Chrome
#             chrome_options.add_argument("--headless=new")
#             chrome_options.add_argument("--no-sandbox")
#             chrome_options.add_argument("--disable-dev-shm-usage")
#             chrome_options.add_argument("--disable-gpu")
#             chrome_options.add_argument("--window-size=1920,1080")
#             chrome_options.add_argument("--disable-extensions")
#             chrome_options.add_argument("--disable-setuid-sandbox")
#             chrome_options.add_argument("--disable-software-rasterizer")
#             chrome_options.add_argument("--disable-notifications")
#
#         driver = webdriver.Chrome(
#             service=ChromeService(ChromeDriverManager().install()),
#             options=chrome_options
#         )
#
#     elif browser == "firefox":
#         firefox_options = FirefoxOptions()
#
#         if IS_CI:
#             # CI-specific options for Firefox
#             firefox_options.add_argument("--headless")
#             firefox_options.add_argument("--width=1920")
#             firefox_options.add_argument("--height=1080")
#
#         driver = webdriver.Firefox(
#             service=GeckoService(GeckoDriverManager().install()),
#             options=firefox_options
#         )
#     else:
#         raise ValueError(f"Unsupported browser: {browser}")
#
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#
#     yield driver
#
#     driver.quit()
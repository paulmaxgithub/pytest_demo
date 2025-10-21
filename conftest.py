import pytest
import warnings
from selenium import webdriver

# urllib3 v2 raises NotOpenSSLWarning when the ssl module is built
# against LibreSSL. Suppress this specific warning during tests.
try:
    from urllib3.exceptions import NotOpenSSLWarning
except Exception:
    NotOpenSSLWarning = None

if NotOpenSSLWarning:
    warnings.filterwarnings("ignore", category=NotOpenSSLWarning)

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()
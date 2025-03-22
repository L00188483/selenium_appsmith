import time

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver

from selenium_appsmith.tests.conftest import SELENIUM_BASE_URL_LOCAL
from selenium_appsmith.tests.conftest import check_appsmith_health, check_selenium_grid_health


def test_gh_action():
    assert True

'''
def test_selenium():
    options = ChromeOptions()
    driver = webdriver.Remote(
        options=options, command_executor=SELENIUM_BASE_URL_LOCAL
    )
    driver.get('https://google.com')
    time.sleep(1)
    assert driver.title == 'Google'
    driver.quit()
'''


def test_service_health():
    assert check_appsmith_health()
    assert check_selenium_grid_health()

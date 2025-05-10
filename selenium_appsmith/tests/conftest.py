import pytest
import time
from urllib.parse import urljoin

import requests


SELENIUM_BASE_URL_LOCAL = "http://localhost:4444"

# Appsmith urls
APPSMITH_BASE_URL_LOCAL = "http://localhost:8080"
APPSMITH_BASE_URL_DOCKER = "http://appsmith:80"
WEBPAGE_URL_PATH = "/app/getting-started-course-v1-app/page1-67df00ef15b9db13e5c83d40"  # got this URL from the "share" button in Appsmith (and made it public)


# old stuff
#WEBPAGE_URL_PATH = "/app/getting-started-course-v1-app/page1-67de9ba6a34c9e557eb0b55f"
#WEBPAGE_URL = "https://app.appsmith.com/app/getting-started-course-v1-app/page1-67dc3444743b81787d0a6ba3?branch=master"


def wait_for_services(timeout):
    """ waits for Appsmith and Selenium-Grid to launch """
    start_time = time.time()
    while time.time() - start_time < timeout:

        asmith_health = check_appsmith_health()
        selenium_health = check_selenium_grid_health()

        if asmith_health and selenium_health:
            return

        time.sleep(2)

    pytest.exit("Appsmith or Selenium-Grid failed to launch")


def check_appsmith_health():
    # appsmith health check: http://localhost:8080/api/v1/health
    url = urljoin(APPSMITH_BASE_URL_LOCAL, '/api/v1/health')
    resp = requests.get(url)
    if resp.status_code != 200:
        return False
    return resp.json()['responseMeta']['success']


def check_selenium_grid_health():
    # selenium health check: 'http://localhost:4444/status'
    url = urljoin(SELENIUM_BASE_URL_LOCAL, '/status')
    resp = requests.get(url)
    if resp.status_code != 200:
        return False
    return resp.json()['value']['ready']



@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    """Runs before tests can begin"""
    wait_for_services(120)

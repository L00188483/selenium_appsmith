import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from selenium_appsmith.webpage_interface_simple import get_tasks, add_task


def _create_browser():
    driver = webdriver.Remote(
        options=Options(), command_executor='http://localhost:4444'
    )
    webpage_url = 'http://localhost:8080/app/getting-started-course-v1-app/page1-67df00ef15b9db13e5c83d40'
    driver.get(webpage_url)
    return driver


def test_add_task():

    driver = _create_browser()

    NEW_TASK_STRING = "Test Task"

    tasks_before = get_tasks(driver)

    add_task(driver, NEW_TASK_STRING)
    time.sleep(1)

    tasks_after = get_tasks(driver)
    new_task = tasks_after[-1]

    assert len(tasks_after) - len(tasks_before) == 1
    assert new_task.text == NEW_TASK_STRING

    # tear down
    driver.quit()






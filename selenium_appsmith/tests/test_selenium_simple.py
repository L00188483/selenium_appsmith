import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from selenium_appsmith.simple_selenium_example import get_tasks, add_task



def test_add_task(page):

    driver = webdriver.Remote(
        options=Options(), command_executor='http://localhost:4444'
    )
    webpage_url = 'http://appsmith:80/app/todo-app/page1-67e8185723be7b0a5efe5ec3'
    driver.get(webpage_url)

    NEW_TASK_STRING = "Test Task"

    tasks_before = get_tasks(driver)

    add_task(driver, NEW_TASK_STRING)

    time.sleep(1)
    tasks_after = get_tasks(driver)

    new_task = tasks_after[-1]

    assert len(tasks_after) - len(tasks_before) == 1
    assert new_task.text == NEW_TASK_STRING

    # cleanup
    driver.quit()





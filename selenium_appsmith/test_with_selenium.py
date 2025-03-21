import time

import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver

from selenium_appsmith.webpage_interface import TodoWebpage


@pytest.fixture
def page():
    options = ChromeOptions()
    driver = webdriver.Remote(
        options=options, command_executor="http://localhost:4444"
    )
    time.sleep(1)

    yield TodoWebpage(driver)
    driver.quit()


def test_add_task(page):
    NEW_TASK_STR = "Test Task"

    tasks_before = page.get_tasks()

    page.add_task(NEW_TASK_STR)

    time.sleep(1)
    tasks_after = page.get_tasks()

    new_task = tasks_after[-1]

    assert len(tasks_after) - len(tasks_before) == 1
    assert new_task.text == NEW_TASK_STR



def test_delete_task(page):
    tasks_before = page.get_tasks()
    first_task_title = tasks_before[0].text

    tasks_before[0].delete()

    time.sleep(1)
    tasks_after = page.get_tasks()
    task_titles_after = [e.text for e in tasks_after]

    assert len(tasks_after) - len(tasks_before) == -1
    assert first_task_title not in task_titles_after


def test_toggle_task_completion(page):
    first_task = page.get_tasks()[0]

    state_before = first_task.is_complete

    first_task.toggle_completion()
    time.sleep(1)
    state_after = first_task.is_complete

    assert state_after != state_before

    first_task.toggle_completion()
    time.sleep(1)
    state_after_2nd_toggle = first_task.is_complete

    assert state_after_2nd_toggle == state_before



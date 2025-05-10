import time
from urllib.parse import urljoin

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium_appsmith.tests.conftest import (
    APPSMITH_BASE_URL_DOCKER, WEBPAGE_URL_PATH, SELENIUM_BASE_URL_LOCAL
)

class TodoWebpage:

    def __init__(self, driver, page_url):
        self.driver = driver
        self.driver.get(page_url)
        time.sleep(3)

    def get_tasks(self):
        task_div_elements = self.driver.find_elements(
            By.CSS_SELECTOR, "div[class*='t--widget-list1_container2']"
        )

        results = []
        for index, div_elem in enumerate(task_div_elements):
            results.append(
                TodoTask(div_elem, index)
            )
        return results

    def add_task(self, text):
        input_element = self.driver.find_element(
            By.CSS_SELECTOR, "input.bp3-input"
        )
        input_element.send_keys(text)
        input_element.send_keys(Keys.RETURN)

    def show_tasks(self):
        for task in self.get_tasks():
            print(task)


class TodoTask:

    def __init__(self, elem, index):
        self.elem = elem
        self.elem_id = elem.id
        self.index = index

    def delete(self):
        trash_icon = self.elem.find_element(
            By.CSS_SELECTOR, "span[icon='trash']"
        )
        trash_icon.click()

    def toggle_completion(self):
        self.elem.click()

    @property
    def is_complete(self):
        html = self.elem.get_attribute('outerHTML')
        return 'text-decoration: line-through' in html

    @property
    def text(self):
        return self.elem.text

    def __repr__(self):
        text = self.text.center(40)[:40]
        return f'{self.index}  |-|  "{text}"  |-|  {self.is_complete}'




def edit_task(elem):
    edit_icon = elem.find_element(By.CSS_SELECTOR, "span[icon='edit']")
    edit_icon.click()
    # todo: incomplete


def main():
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium import webdriver
    options = ChromeOptions()
    driver = webdriver.Remote(
        options=options, command_executor=SELENIUM_BASE_URL_LOCAL
    )

    webpage_url = urljoin(APPSMITH_BASE_URL_DOCKER, WEBPAGE_URL_PATH)
    page = TodoWebpage(driver, webpage_url)
    tasks = page.get_tasks()

    breakpoint()

    driver.quit()


if __name__ == '__main__':
    main()

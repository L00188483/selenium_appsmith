import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver


def add_task(driver, text):
    input_element = driver.find_element(By.CSS_SELECTOR, "input.bp3-input")

    input_element.send_keys(text)
    input_element.send_keys(Keys.RETURN)


def delete_task(elem):
    trash_icon = elem.find_element(By.CSS_SELECTOR, "span[icon='trash']")
    trash_icon.click()


def toggle_task_completion(elem):
    elem.click()


def get_tasks(driver):
    results = {}

    task_div_elements = driver.find_elements(
        By.CSS_SELECTOR, "div[class*='t--widget-list1_taskcontainer']"
    )
    for div_elem in task_div_elements:
        outer_html = div_elem.get_attribute('outerHTML')
        id = div_elem.id # selenium temporary id

        results[id] = {
            'elem': div_elem,
            'text': div_elem.text,
            'is_complete': 'text-decoration: line-through' in outer_html,
        }

    return results


'''
def edit_task(elem):
    edit_icon = elem.find_element(By.CSS_SELECTOR, "span[icon='edit']")
    edit_icon.click()
    # todo: incomplete
'''


def main():
    options = ChromeOptions()
    driver = webdriver.Remote(
        options=options, command_executor="http://localhost:4444"
    )

    driver.get("https://app.appsmith.com/app/getting-started-course-v1-app/page1-67dc3444743b81787d0a6ba3?branch=master")


    import pdb; pdb.set_trace()

    driver.quit()


if __name__ == '__main__':
    main()

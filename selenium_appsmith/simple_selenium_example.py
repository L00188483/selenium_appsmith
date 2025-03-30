import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def add_task(driver, text):
    input_element = driver.find_element(
        By.CSS_SELECTOR, "input.bp3-input"
    )
    input_element.send_keys(text)
    input_element.send_keys(Keys.RETURN)

def delete_task(driver, index):
    task_div_elements = driver.find_elements(
        By.CSS_SELECTOR, "div[class*='t--widget-list1_container2']"
    )
    for i, elem in enumerate(task_div_elements):
        if i == index:
            trash_icon = elem.find_element(
                By.CSS_SELECTOR, "span[icon='trash']"
            )
            trash_icon.click()

def get_tasks(driver):
    task_div_elements = driver.find_elements(
        By.CSS_SELECTOR, "div[class*='t--widget-list1_container2']"
    )
    return [elem.text for elem in task_div_elements]

def main():
    driver = webdriver.Remote(
        options=Options(), command_executor='http://localhost:4444'
    )
    webpage_url = 'http://appsmith:80/app/todo-app/page1-67e8185723be7b0a5efe5ec3'
    driver.get(webpage_url)

    add_task(driver, 'finish assignment')
    tasks = get_tasks(driver)
    print(tasks)


    breakpoint()


if __name__ == '__main__':
    main()

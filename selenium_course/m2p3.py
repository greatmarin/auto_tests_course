import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Нажать на кнопку
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    # Новая вкладка
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    # Решить капчу для роботов на новой странице
    time.sleep(1)  # Дать странице загрузиться

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    answer = calc(x)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(answer)

    # Нажать на кнопку "Submit"
    submit_button = browser.find_element(By.CLASS_NAME, "btn")
    submit_button.click()

finally:
    # Подождать, чтобы увидеть результат
    time.sleep(10)
    browser.quit()

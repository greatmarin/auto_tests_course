from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ожидание, пока цена не станет $100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажатие на кнопку "Book"
    button = browser.find_element(By.ID, "book")
    button.click()

    # Решение капчи для роботов
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    answer = calc(x)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(answer)

    # Нажатие на кнопку "Submit"
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    # Ожидание появления результата
    #message = WebDriverWait(browser, 10).until(
    #    EC.presence_of_element_located((By.TAG_NAME, "h1"))
    #)

    #assert "successful" in message.text

finally:
    time.sleep(5)
    browser.quit()
from selenium.webdriver.common.by import By

def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(add_to_basket_button) > 0, "Add to basket button is not present"
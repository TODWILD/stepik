from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value.nowrap")
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)

    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()

    option2 = browser.find_element_by_css_selector("[value='robots']")
    option2.click()


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

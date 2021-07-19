from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#num1")
    x = x_element.text
    y_element = browser.find_element_by_css_selector("#num2")
    y = y_element.text
    z= str(int(x)+int(y))

    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("[value='"+ z +"']").click()


    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(30)
    browser.quit()

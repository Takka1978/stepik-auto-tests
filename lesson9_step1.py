from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link="http://suninjuly.github.io/alert_accept.html"
try:
    browser=webdriver.Chrome()
    browser.get(link)
    button=browser.find_element_by_css_selector("[type='submit']")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element_by_css_selector("span#input_value")
    x = x_element.text
    y = calc(x)
    input1=browser.find_element_by_id("answer")
    input1.send_keys(y)
    button1=browser.find_element_by_css_selector("[type='submit']")
    button1.click()          

finally:
    time.sleep(10)
    browser.quit()
    
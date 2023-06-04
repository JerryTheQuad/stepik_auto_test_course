from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(0.5)

    alert = browser.switch_to.alert.accept()

    time.sleep(0.5)

    x_element = browser.find_element(By.TAG_NAME, "span[id='input_value']")
    y = calc(x_element.text)

    time.sleep(0.5)

    input2 = browser.find_element(By.TAG_NAME, "input[name='text']")
    input2.click()
    input2.send_keys(y)

    time.sleep(0.5)

    input3 = browser.find_element(By.CSS_SELECTOR, "button.btn").click()



finally:
    time.sleep(10)
    browser.quit()

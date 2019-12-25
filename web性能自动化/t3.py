from selenium import webdriver
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
chrome_driver = PATH("exe/chromedriver.exe")
os.environ["webdriver.chrome.driver"] = chrome_driver
driver = webdriver.Chrome(chrome_driver)
driver.get("http://www.baidu.com")
# data = driver.execute_script("return window.performance.getEntries();")
data = driver.execute_script("return window.performance.timing;")
print(data)

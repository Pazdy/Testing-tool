import os
from selenium import webdriver

os.environ['PATH'] += r"C:\Users\HP\PycharmProjects\Testing-tool\chrome-driver"
browser = "chrome"

class steps():
    def __init__(self, browser):
        self.browser = browser()
        pass
    pass

if browser == "chrome":
    browser = webdriver.Chrome
elif browser == "firefox":
    browser = webdriver.Firefox()
elif browser == "edge":
    browser = webdriver.Edge()

driver = steps(browser)
#importing importante libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import excelimport as ei

#path where is stored chrome driver
PATH = Service(r"C:\Users\HP\PycharmProjects\Testing-tool\chrome-driver\chromedriver.exe")

#configuration from excel in dict
config = ei.actarg

class Steps:
    def actions(self):
        for keys in config:
            if keys == "Browser":
                self.chosebrowser()
                pass
            elif keys == "URL":
                self.gourl()
                pass
            elif keys == "End":
                print("ano")
                pass
            else:
                continue
            pass
        pass
    def chosebrowser(self):
        for keys, values in config.items():
            if values == "Chrome":
                self.driver = webdriver.Chrome
                pass
            pass
        pass
    def gourl(self):
        for keys, values in config.items():
            if keys == "URL":
                self.driver(service=PATH).get(url=values)
                pass
            pass
        pass
    pass

testcase = Steps()

testcase.actions()












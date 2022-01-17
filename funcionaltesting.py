#importing importante libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import excelimport as ei
import time

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
            elif keys == "Search": # id(unique), name(usually unique), class(not always unique), Tag
                self.searchbar()
                pass
            elif keys == "Whatsearch":
                self.whatsearch()
                pass
            elif keys == "Button":
                self.button()
            elif keys == "End":
#                time.sleep(5)
#                self.driver.quit()
                pass
            else:
                continue
            pass
        pass
    def chosebrowser(self):
        for keys, values in config.items():
            if values == "Chrome":
                self.driver = webdriver.Chrome(service=PATH)
                pass
            pass
        pass
    def gourl(self):
        for keys, values in config.items():
            if keys == "URL":
                self.gurl =self.driver.get(url=values)
                pass
            pass
        pass
    def searchbar(self):
        for keys, values in config.items():
            if keys == "Search":
                self.searchbox = self.driver.find_element(By.XPATH, value=values)
            else:
                continue
    def whatsearch(self):
        for keys, values in config.items():
            if keys == "Whatsearch":
                self.searchbox.send_keys(values)
            else:
                continue
            pass
        pass
    def button(self):
        for keys, values in config.items():
            if keys == "Button":
                self.click = self.driver.find_element(By.XPATH, value= values)
                time.sleep(5)
                self.click.click()
    pass

testcase = Steps().actions()













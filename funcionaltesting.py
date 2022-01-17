#importing importante libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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
            elif keys == "Search": # id(unique), name(usually unique), class(not always unique), Tag
                print("ano")
                self.searchbar()
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
                self.searchbox.send_keys("Mobil")
            else:
                continue
    pass

testcase = Steps().actions()













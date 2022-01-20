# importing importante libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from excelimport import configuration
import time

# path where is stored chrome driver
PATH = Service(r"C:\Users\HP\PycharmProjects\Testing-tool\chrome-driver\chromedriver.exe")

# class Test_case stands for logic of program (store all methods)


class Testcase:
    # testexecution method works with nested lists-> every nested list represents one step that needs to be processed
    def testexcecution(self):
        # looping over all steps in the configuration
        for step in range(len(configuration)):
            # looping over all actions in step
            for action in configuration[step]:
                # catches step you are work with
                self.step = step
                # what action should be processed
                if action == "Browser":
                    self.chosebrowser()
                    pass
                elif action == "URL":
                    self.gourl()
                    pass
                elif action == "Search":
                    self.searchbar()
                    pass
                elif action == "Button":
                    self.button()
                    pass
                elif action == "End":
                    time.sleep(5)
                    self.driver.quit()
                    pass
                else:
                    continue
                pass
        pass

    # method that stands for opening wanted browser filled in config

    def chosebrowser(self):
        # same looping as in test excecution
        if configuration[self.step][1] == "Chrome":
            # choose webdriver as chrome
            self.driver = webdriver.Chrome(service=PATH)

        elif configuration[self.step][1] == "Edge":
            self.driver = webdriver.Edge(service=PATH)

        elif configuration[self.step][1] == "Firefox":
            self.driver = webdriver.Firefox(service=PATH)

        elif configuration[self.step][1] == "Safari":
            self.driver = webdriver.Safari(service=PATH)
        else:
            print("Putted wrong browser")
        pass
    # method that stands for visiting web which put user to config

    def gourl(self):
        # redirect to web
        self.driver.get(url=configuration[self.step][1])

    # find element of searchbar then fill it with the string putted in config
    def searchbar(self):
        # find specific element on the page
        self.locators()
        self.searchbox = self.locator
        # put string from confid to the searchbar
        self.searchbox.send_keys(configuration[self.step][3])

    # button method that first find element to click then click

    def button(self):
        self.locators()
        self.element = self.locator
        time.sleep(3)
        self.element.click()

    # locators method decide according to configuration by which element gonna be used for searching
    # and also takes value for it

    def locators(self):
        if configuration[self.step][1] == "XPath":
            self.locator = self.driver.find_element(By.XPATH, value=configuration[self.step][2])

        elif configuration[self.step][1] == "ID":
            self.locator = self.driver.find_element(By.ID, value=configuration[self.step][2])

        elif configuration[self.step][1] == "Class":
            self.locator = self.driver.find_element(By.CLASS_NAME, value=configuration[self.step][2])

        elif configuration[self.step][1] == "Link":
            self.locator = self.driver.find_element(By.LINK_TEXT, value=configuration[self.step][2])

        elif configuration[self.step][1] == "Name":
            self.locator = self.driver.find_element(By.NAME, value=configuration[self.step][2])

        elif configuration[self.step][1] == "Tag":
            self.locator = self.driver.find_element(By.TAG_NAME, value=configuration[self.step][2])

        elif configuration[self.step][1] == "CSS_Selector":
            self.locator = self.driver.find_element(By.CSS_SELECTOR, value=configuration[self.step][2])

        elif configuration[self.step][1] == "Partial_Link":
            self.locator = self.driver.find_element(By.PARTIAL_LINK_TEXT, value=configuration[self.step][2])
        else:
            print("Error Locators")
        pass
    pass


Testcase().testexcecution()


# id(unique), name(usually unique), class(not always unique), Tag

# importing importante libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from excelimport import configuration
import time

# path where is stored chrome driver
PATH = Service(r"C:\Users\HP\PycharmProjects\Testing-tool\chrome-driver\chromedriver.exe")

# class Test_case stands for logic of program (store all methods)


class Testcases():
    # testexecution method works with nested lists-> every nested list represents one step that needs to be processed
    def test_excecutions(self):
        # looping over all steps in the configuration
        for step in range(len(configuration)):
            # looping over all actions in step
            for action in configuration[step]:
                print(action)
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
                    time.sleep(3)
                    self.clicks()
                    pass
                elif action == "Select":
                    pass
                elif action == "Back":
                    self.back()
                elif action == "Forward":
                    self.forward()
                elif action == "Clear":
                    self.clear()
                elif action == "End":
                    self.driver.quit()
                    pass
                elif action == "Wait":
                    self.wait()
                elif action == "Title":
                    self.title()
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

    def clicks(self):
        try:
            self.locators()
            self.element = self.locator
            self.element.click()
        except:
            self.driver.quit()
            print("Spatný locator")

    # locators method decide according to configuration by which element gonna be used for searching
    # and also takes value for it

    def locators(self):
        if configuration[self.step][1] == "XPath":
            self.locator = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, configuration[self.step][2])))

        elif configuration[self.step][1] == "ID":
            self.locator = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, configuration[self.step][2])))

        elif configuration[self.step][1] == "Class":
            self.locator = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, configuration[self.step][2])))

        elif configuration[self.step][1] == "Link":
            self.locator = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, configuration[self.step][2])))

        elif configuration[self.step][1] == "Name":
            self.locator = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, configuration[self.step][2])))

        elif configuration[self.step][1] == "Tag":
            self.locator = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.TAG_NAME, configuration[self.step][2])))

        elif configuration[self.step][1] == "CSS_Selector":
            self.locator = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, configuration[self.step][2])))

        elif configuration[self.step][1] == "Partial_Link":
            self.locator = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, configuration[self.step][2])))
        else:
            print("Error Locators")
    def select(self):
        self.locators()
        self.element = self.locator
        pass
    pass

    def back(self):
        for i in range(int(configuration[self.step][1])):
            self.driver.back()
        pass
    pass

    def forward(self):
        for i in range(int(configuration[self.step][1])):
            self.driver.forward()
        pass
    pass

    def clear(self):
       self.clearence = self.searchbox.clear()

    def wait(self):
        self.waiting = time.sleep(configuration[self.step][1])

    def title(self):
        if configuration[self.step][1] == self.driver.title:
            self.titleO = print("Y")
        else:
            self.titleO = print("N")


Testcases().test_excecutions()

# id(unique), name(usually unique), class(not always unique), Tag

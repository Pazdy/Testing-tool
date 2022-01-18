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
        for step in range(len(configuration)):
            for action in configuration[step]:
                if action == "Chrome":
                    # choose webdriver as chrome
                    self.driver = webdriver.Chrome(service=PATH)
                else:
                    continue
                pass
            pass
        pass
    # method that stands for visiting web which put user to config

    def gourl(self):

        # same looping as in test excecution
        for step in range(len(configuration)):
            for action in configuration[step]:
                if action == "URL":
                    # redirect to web
                    self.driver.get(url=configuration[step][1])
                    pass
                else:
                    continue
                pass
            pass
        pass
    # search

    def searchbar(self):
        for step in range(len(configuration)):
            for action in configuration[step]:
                if action == "Search":
                    self.searchbox = self.driver.find_element(By.XPATH, value=configuration[step][2])
                    self.searchbox.send_keys(configuration[step][3])
                else:
                    continue

    def button(self):
        for step in range(len(configuration)):
            for action in configuration[step]:
                if action == "Button":
                    if configuration[step][1] == "XPath":
                        self.click = self.driver.find_element(By.XPATH, value=configuration[step][2])
                        time.sleep(3)
                        self.click.click()

                    elif configuration[step][1] == "ID":
                        self.click = self.driver.find_element(By.ID, value=configuration[step][2])
                        time.sleep(3)
                        self.click.click()

                    elif configuration[step][1] == "Class":
                        self.click = self.driver.find_element(By.CLASS_NAME, value=configuration[step][2])
                        time.sleep(3)
                        self.click.click()

                    else:
                        print("You put wrong element in configuration")
                else:
                    continue
                    pass
                pass
            pass
        pass
    pass


Testcase().testexcecution()


# id(unique), name(usually unique), class(not always unique), Tag

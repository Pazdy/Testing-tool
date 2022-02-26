# importing important libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


# class Testcases stands for logic of program (store all methods)
class Testcases():
    # test execution method execute execute test
    def test_excecution(self, configuration, path, opath, test):
        # result store test file, steps, errors
        self.result = []
        self.result.append(test)
        # If config gonna be empty then to the result will be added comment about that
        if configuration == []:
            self.result.append("Konfigurace je prázdná, je potřeba vložit argumenty a parametry dle dokumentace!")

        # Step "Browser" must be first in config and URL must be second step in config
        elif configuration[0][0].upper() == "BROWSER" and configuration[1][0].upper() == "URL":

            # Try to loop over config
            try:

                # Looping over configuration
                for step in configuration:
                    self.step = step
                    print(step)
                    if "BROWSER" == step[0].upper():
                        self.result.append(self.step)
                        if self.step[1] == "Chrome":
                            self.driver = webdriver.Chrome(service=Service(path))

                        elif self.step[1] == "Edge":
                            self.driver = webdriver.Edge(service=Service(path))

                        elif self.step[1] == "Safari":
                            self.driver = webdriver.Safari(service=Service(path))
                        pass
                    elif "URL" == step[0].upper():
                        self.result.append(self.step)
                        self.gourl()
                        pass
                    elif "INPUT" in step[0].upper():
                        self.result.append(self.step)
                        self.input_text()
                        pass
                    elif "BUTTON" in step[0].upper():
                        self.result.append(self.step)
                        self.clicks()
                    elif "BACK" in step[0].upper():
                        self.result.append(self.step)
                        self.back(configuration)
                    elif "FORWARD" in step[0].upper():
                        self.result.append(self.step)
                        self.forward(configuration)
                    elif "CLEAR" in step[0].upper():
                        self.result.append(self.step)
                        self.clear()
                        pass
                    elif "END" == step[0].upper():
                        self.result.append("Test uspěšně proveden!")
                        self.driver.quit()
                        break
                    elif "WAIT" in step[0].upper():
                        self.result.append(self.step)
                        self.wait()
                    # think about this
                    elif "TITLE" in step[0].upper():
                        self.check_title()
                    elif "MAX" in step[0].upper():
                        self.max()
                        pass

                    # If there will be step which is not recognized then else runs -> result of it saved in result var.
                    else:
                        self.result.append(step[0])
                        self.result.append("Neznamý krok! Projdi dokumentaci pro seznam kroků a jejich parametry.")
                        self.driver.quit()
                        break

            # If in loop gonna be any issue program will run expect code
            except:
                # If third step in config will be steps that cannot be processed then it will be save to result var.
                if configuration[2][0].upper() not in ("WAIT", "BUTTON", "SEARCH", "TITLE", "MAX"):
                    self.result.append("Krok v konfiguraci musí obsahovat krok, který se dá provést! "
                                       "Pro nápovědu použij dokumentaci.")
                    self.driver.quit()

                # If will be error in any step of config then it will be saved in result var.
                elif self.step[0].upper() not in ("BUTTON", "SEARCH"):
                    self.result.append("V kroku " + self.step[0] + " nastala chyba! "
                                                                   "Pro správné spuštění oprav chybu."
                                                                   " Zkontroluj parametry."
                                                                   " Pro nápovědu použij dokumentaci.")
                    self.driver.quit()
        # If first two steps will not be "Browser" and "URL" else will be execute
        else:
            self.result.append("Počáteční krok musí být Browser a následovat musí URL! "
                               "Pro nápovědu projdi dokumentaci.")
            pass

        self.append_to_result(opath)

    # appending to excel(result file) result of test
    def append_to_result(self, opath):
        self.df_now = pd.read_excel(opath)
        self.df_now.append([self.result]).to_excel(opath, index=False)

    def gourl(self):
        self.driver.get(url=self.step[1])

    # find element a insert input
    def input_text(self):
        self.locators()
        self.location = self.locator

        # put string from confid to the searchbar
        self.location.send_keys(self.step[3])

    # button method that first find element to click then click
    def clicks(self):
        self.locators()
        self.element = self.locator
        self.element.click()
    # locators method decide according to configuration by which element gonna be used for searching
    # and also takes value for it ->result of this is unique identificator on the page

    def locators(self):
        try:
            if self.step[1].upper() == "XPATH":
                self.locator = WebDriverWait(self.driver, 5).\
                    until(EC.element_to_be_clickable((By.XPATH, self.step[2])))

            elif self.step[1].upper() == "ID":
                self.locator = WebDriverWait(self.driver, 3).\
                    until(EC.element_to_be_clickable((By.ID, self.step[2])))

            elif self.step[1].upper() == "CLASS":
                self.locator = WebDriverWait(self.driver, 3).\
                    until(EC.element_to_be_clickable((By.CLASS_NAME, self.step[2])))

            elif self.step[1].upper() == "LINK":
                self.locator = WebDriverWait(self.driver, 3).\
                    until(EC.element_to_be_clickable((By.LINK_TEXT, self.step[2])))

            elif self.step[1].upper() == "NAME":
                self.locator = WebDriverWait(self.driver, 3).\
                    until(EC.element_to_be_clickable((By.NAME, self.step[2])))

            elif self.step[1].upper() == "TAG":
                self.locator = WebDriverWait(self.driver, 3).\
                    until(EC.element_to_be_clickable((By.TAG_NAME, self.step[2])))

            elif self.step[1].upper() == "CSSSELECTOR":
                self.locator = WebDriverWait(self.driver, 3).\
                    until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.step[2])))

            elif self.step[1].upper() == "PARTLINK":
                self.locator = WebDriverWait(self.driver, 3).\
                    until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.step[2])))
            else:
                self.result.append("Chyba v názvu lokátoru!")
                self.driver.quit()
        except:
            self.result.append("Chyba v cestě lokátoru!")
            self.driver.quit()

    def back(self, configuration):
        for i in range(int(configuration[self.step][1])):
            self.driver.back()
        pass
    pass

    def forward(self, configuration):
        for i in range(int(configuration[self.step][1])):
            self.driver.forward()
        pass
    pass

    def clear(self):
        self.location.clear()

    def wait(self):
        time.sleep(int(self.step[1]))

    def check_title(self):
        if self.step[1] == self.driver.title:
            self.result.append("Titulek souhlasí!")
        else:
            self.result.append("Titulek nesouhlasí!")

    def max(self):
        self.driver.maximize_window()
        pass
    pass


# id(unique), name(usually unique), class(not always unique), Tag

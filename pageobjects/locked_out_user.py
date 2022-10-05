from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver import ActionChains
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *

class locked_outPageObject(PageObject):
    def init_page_elements(self):
        self.username = Button(By.XPATH, "//*[@id='user-name']")
        self.password = Button(By.XPATH, "//*[@id='password']")
        self.login_button = Button(By.XPATH, "//*[@id='login-button']")

    def open(self):  # opens browser
        self.driver\
            .get('https://www.saucedemo.com/')
        return self

    def name(self):
        self.username\
            .click()
        return self

    def enter_name(self):
        ActionChains(self.driver)\
            .send_keys("locked_out_user")\
            .perform()
        return self

    def passwordd(self):
        self.password\
            .click()
        return self

    def enter_passwrd(self):
        ActionChains(self.driver)\
            .send_keys("secret_sauce")\
            .perform()
        return self

    def button(self):
        self.login_button\
            .click()
        return self

    def locked_out_message_error(self):
        self.locked_out_message_err = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        return self.locked_out_message_err.text



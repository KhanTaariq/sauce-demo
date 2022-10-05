from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver import ActionChains
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class Problem_UserPageObject(PageObject):
    def init_page_elements(self):
        self.username = Button(By.XPATH, "//*[@id='user-name']")
        self.password = Button(By.XPATH, "//*[@id='password']")
        self.login_button = Button(By.XPATH, "//*[@id='login-button']")
        self.problem_title_products = Button(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/span")

    def open(self):  # opens browser
        self.driver\
            .get('https://www.saucedemo.com/')
        return self

    def name(self):
        self.username.click()
        return self

    def enter_name(self):
        ActionChains(self.driver)\
            .send_keys("problem_user")\
            .perform()
        return self

    def passwordd(self):
        self.password\
            .click()
        return self

    def enter_p_word(self):
        ActionChains(self.driver)\
            .send_keys("secret_sauce")\
            .perform()
        return self

    def button(self):
        self.login_button\
            .click()
        return self

    def problem_user_title_products(self):
        self.problem_title_products\
            .is_present()
        return self
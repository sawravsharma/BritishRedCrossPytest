import sys, os
import time
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import xlrd
from Locators.Locators import Locators
from Config.config import TestData
from Pages.BasePage import BasePage

class LoginPage(BasePage):

    '''constructor of the page class'''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    '''Page Actions for login page'''
    '''this method is use to get the page title'''
    def get_login_page_title(self, title):
        self.driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()
        return self.get_title(title)

    '''this is use to login to application'''
    def do_login(self):
            self.driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()
            self.do_click(Locators.CLICK_ON_MY_ACCOUNT)
            self.do_send_keys(Locators.EMAIL, TestData.USERNAME)
            self.do_send_keys(Locators.PASSWORD, TestData.PASSWORD)
            self.do_click(Locators.LOGIN_BUTTON)

    # def logged_in_user(self):
    #     # self.driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()
    #     return self.get_element_text(Locators.LOGGED_IN_USER)
    
    # '''this is use to login to application with incorrect credentials'''
    # def do_login_with_incorrect_credentials(self):
    #         self.do_click(Locators.CLICK_ON_MY_ACCOUNT)
    #         time.sleep(3)
    #         self.do_send_keys(Locators.EMAIL, TestData.INC_USERNAME)
    #         time.sleep(3)
    #         self.do_send_keys(Locators.PASSWORD, TestData.INC_PASSWORD)
    #         self.do_click(Locators.LOGIN_BUTTON)
    
    def do_logout(self):
        self.do_click(Locators.CLICK_ON_MY_ACCOUNT)
        self.do_click(Locators.LOGOUT_BUTTON)
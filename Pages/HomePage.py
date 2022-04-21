
import os,sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
from Locators.Locators import Locators
from Pages.BasePage import BasePage
from EnumsPackage.Enums import Beauty, Clothing, Homeware, Stationery
from selenium.webdriver.common.action_chains import ActionChains

class HomePage(BasePage):
 
    def __init__(self, driver):
        super().__init__(driver)

    # '''Title'''
    # def get_home_page_title(self, title):
    #     return self.get_title(title)

    # '''To check Cart icon'''
    # def is_cart_icon_exist(self):
    #     return self.is_visible(Locators.CART_ICON)

    # '''To get h1 tag text'''
    # def get_header_value(self):
    #     return self.get_element_text(Locators.HEADER)

    '''Product sorting container functionality'''
    def clickClothingTab(self):
        self.driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()
        for sorting in Clothing:
            element = self.driver.find_element_by_link_text("Clothing")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            sorting = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(sorting.value))
            time.sleep(3)
            sorting.click()
        # self.driver.find_element_by_xpath("(//a[@href = '/account/login'])[2]").click()
        # self.driver.find_element_by_xpath("//*[@id='account-popover']/div/div/a[4]").click()

    def clickHomeWareTab(self):
        for sorting in Homeware:
            element = self.driver.find_element_by_link_text("Homeware")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            sorting = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(sorting.value))
            time.sleep(3)
            sorting.click()

    def clickStationeryTab(self):
        for sorting in Stationery:
            element = self.driver.find_element_by_link_text("Stationery")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            sorting = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(sorting.value))
            time.sleep(3)
            sorting.click()

    def clickBeautyTab(self):
        for sorting in Beauty:
            element = self.driver.find_element_by_link_text("Beauty")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            sorting = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(sorting.value))
            time.sleep(3)
            sorting.click()

    def do_logout(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'My account ')]").click()
        time.sleep(3)
        self.do_click(Locators.LOGOUT_BUTTON)
    




import os,sys

import pytest
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
from Locators.Locators import Locators
from Pages.BasePage import BasePage
from EnumsPackage.Enums import Beauty, Clothing, DisplayPerPage, Homeware, Stationery, TshirtsAndSweatShirts, TshirtsAndSweatShirtsSorting, VirtualGifts
from selenium.webdriver.common.action_chains import ActionChains

class HomePage(BasePage):
 
    def __init__(self, driver):
        super().__init__(driver)

    '''Title'''
    def get_home_page_title(self, title):
        return self.get_title(title)

    # '''To check Cart icon'''
    # def is_cart_icon_exist(self):
    #     return self.is_visible(Locators.CART_ICON)

    # '''To get h1 tag text'''
    # def get_header_value(self):
    #     return self.get_element_text(Locators.HEADER)

    '''Product sorting container functionality'''
    def clickClothingTab(self):
        # self.driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()
        for sorting in Clothing:
            element = self.driver.find_element_by_link_text("Clothing")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            sorting = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(sorting.value))
            # time.sleep(3)
            sorting.click()

    def clickHomeWareTab(self):
        for sorting in Homeware:
            element = self.driver.find_element_by_link_text("Homeware")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            sorting = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(sorting.value))
            # time.sleep(3)
            sorting.click()

    def clickStationeryTab(self):
        for sorting in Stationery:
            element = self.driver.find_element_by_link_text("Stationery")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            sorting = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(sorting.value))
            # time.sleep(3)
            sorting.click()

    def clickBeautyTab(self):
        for sorting in Beauty:
            element = self.driver.find_element_by_link_text("Beauty")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            sorting = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(sorting.value))
            # time.sleep(3)
            sorting.click()
    
    def clickShopHomeTab(self):
        self.driver.find_element_by_link_text("Shop Home")

    def clickNewInTab(self):
        self.driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()
        self.driver.find_element_by_link_text("New In")
        self.driver.find_element_by_xpath("//button[@class='value-picker-button']//span[contains(text(),'Display')]").click()
        for page in DisplayPerPage:
            page = self.driver.find_element_by_xpath("//button[@data-value=%s]" % int(page.value))
            page.click()

    def clickVirtualGiftsTab(self):
        self.driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()
        self.driver.find_element_by_link_text("Virtual Gifts").click()
        for gift in VirtualGifts:
            giftEle = self.driver.find_element_by_xpath(
                "//span[contains(text(),'%s')]/following-sibling::a[contains(text(),'Send now')]" % str(gift.value))
            giftEle.click()
            print(gift)
            # self.driver.switch_to.frame("_hjRemoteVarsFrame")
            # self.driver.implicitly_wait(10)
            # self.driver.find_element_by_xpath("//span[text()='Congrats']").click()
            self.driver.implicitly_wait(10)
            self.driver.switch_to.alert().text("testing")
            # self.driver.find_element_by_xpath("//*[@id='only-message']").send_keys("Hey")
            self.driver.find_element_by_xpath(
                "//div[@class='product-form__payment-container']//button[text()='Add to cart']").click()
            self.driver.find_element_by_link_text("Virtual Gifts").click()

    def clickSaleTab(self):
        self.driver.find_element_by_link_text("Sale")

    def clickTshirtsAndSweatShirtsTab(self):
        self.driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()
        element = self.driver.find_element_by_link_text("Clothing")
        action = ActionChains(self.driver)
        action.click(on_element = element)
        action.perform()
        Tees = self.driver.find_element_by_xpath(
            "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Clothing.CLOTHING_Name_TShirt.value))
        Tees.click()
        for cloth in TshirtsAndSweatShirts:
            cloth = self.driver.find_element_by_xpath("//a[contains(text(),'%s')]" % str(cloth.value))
            cloth.click()
            time.sleep(3)
            self.driver.find_element_by_xpath(
                "//div[@class='product-form__payment-container']//button[text()='Add to cart']").click()
            element = self.driver.find_element_by_link_text("Clothing")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            Tees = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Clothing.CLOTHING_Name_TShirt.value))
            Tees.click()

    '''Product sorting container functionality'''
    def sortingProducts(self):
        self.driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()
        self.driver.find_element_by_xpath("//*[@id='shopify-section-header']/section/nav/div/div/ul/li[2]/a").click()
        time.sleep(5)
        # self.driver.find_element_by_xpath("//span[contains(text(),'Sort by')]").click()
        element = self.driver.find_element_by_xpath("//button[contains(text(),'Sort by')]")
        action = ActionChains(self.driver)
        action.click(on_element = element)
        action.perform()
        for sorting in TshirtsAndSweatShirtsSorting:
            sorting = self.driver.find_element_by_xpath(
                "//button[contains(text(),'%s')]" % str(sorting.value))
            sorting.click()

    def do_logout(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'My account ')]").click()
        # time.sleep(3)
        self.do_click(Locators.LOGOUT_BUTTON)
    



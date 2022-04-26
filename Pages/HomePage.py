
# import os,sys
# myPath = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, myPath + '/../')

from ast import Assert
import time
import string
import random

from EnumsPackage.EnamelPin import EnamelPin
from EnumsPackage.FoodDrinks import FoodAndDrinks
from Locators.Locators import Locators
from Pages.BasePage import BasePage
from EnumsPackage.Clothing import Clothing
from selenium.webdriver.common.action_chains import ActionChains
from EnumsPackage.Beauty import Beauty
from EnumsPackage.DisplayPerPage import DisplayPerPage
from EnumsPackage.Homeware import Homeware
from EnumsPackage.Stationery import Stationery
from EnumsPackage.TshirtsAndSweatShirtsSorting import TshirtsAndSweatShirtsSorting
from EnumsPackage.Emolyne import Emolyne

from EnumsPackage.TshirtsAndSweatShirts import TshirtsAndSweatShirts

class HomePage(BasePage):
 
    def __init__(self, driver):
        super().__init__(driver)

    '''Title'''
    def get_home_page_title(self, title):
        return self.get_title(title)

    '''To check Cart icon'''
    def is_cart_icon_exist(self):
        self.if_alert()
        return self.is_visible(Locators.CART_ICON)

    '''Product sorting container functionality'''
    def clickClothingTab(self):
        self.if_alert()
        for sorting in Clothing:
            element = self.driver.find_element_by_link_text("Clothing")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            sorting = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(sorting.value))
            sorting.click()

    def clickHomeWareTab(self):
        self.if_alert()
        for sorting in Homeware:
            element = self.driver.find_element_by_link_text("Homeware")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            sorting = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(sorting.value))
            sorting.click()

    def clickStationeryTab(self):
        self.if_alert()
        for sorting in Stationery:
            element = self.driver.find_element_by_link_text("Stationery")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            sorting = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(sorting.value))
            sorting.click()

    def clickBeautyTab(self):
        # self.if_alert()
        for sorting in Beauty:
            element = self.driver.find_element_by_link_text("Beauty")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            sorting = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(sorting.value))
            sorting.click()
    
    def clickShopHomeTab(self):
        # element_found = []
        self.if_alert()
        self.driver.find_element_by_link_text("Shop Home")
        self.driver.find_element_by_xpath("(//a[@href='/collections/new-in'])[5]").click()
        # select = Select(self.driver.find_elements_by_xpath("//button[@class='value-picker-button']//span[contains(text(),'Display')]"))
        # select.select_by_visible_text("Display: 24 per page")
        self.driver.find_element_by_xpath("//button[@class='value-picker-button']//span[contains(text(),'Display')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='display-by-selector']/div/div/button[1]").click()
        time.sleep(5)
        element_found = self.driver.find_elements_by_xpath("//div[@class='product-item product-item--vertical  1/3--tablet-and-up 1/3--desk']")
        print(len(element_found))
        assert len(element_found) == 24

    '''asserting 24 elements filter per page'''
    def clickNewInTab(self):
        self.if_alert()
        self.driver.find_element_by_xpath("(//*[text()='New In '])[2]").click()
        self.driver.find_element_by_xpath("//button[@class='value-picker-button']//span[contains(text(),'Display')]").click()
        page = self.driver.find_element_by_xpath("//button[contains(text(),'%s')]" % str(DisplayPerPage.Display_per_page_24.value))
        page.click()
        element_found = self.driver.find_elements_by_xpath("//div[@class='product-item product-item--vertical  1/3--tablet-and-up 1/3--desk']")
        print(len(element_found))
        assert len(element_found) == 24

    def clickVirtualGiftsTab(self):
        self.if_alert()
        self.driver.find_element_by_link_text("Virtual Gifts").click()

    def clickSaleTab(self):
        self.if_alert()
        self.driver.find_element_by_link_text("Sale")

    def clickOnCartButton(self):
        self.if_alert()
        self.driver.find_element_by_xpath("//*[text()='Cart']").click()

    '''Product sorting container functionality'''
    def sortingProducts(self):
        self.if_alert()
        self.driver.find_element_by_xpath("(//*[text()='New In '])[2]").click()
        self.driver.find_element_by_xpath("(//div[@class='value-picker-wrapper']//span[contains(text(),'Sort by')])[1]").click()
        time.sleep(5)
        sorting = self.driver.find_element_by_xpath(
                "//button[contains(text(),'%s')]" % str(TshirtsAndSweatShirtsSorting.Alphabetically_A_to_Z.value))
        sorting.click()

    def do_logout(self):
        self.if_alert()
        self.do_click(Locators.LOGOUT_BUTTON)

    def clickTshirtsAndSweatShirtsTab(self):
        self.if_alert()
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

    def addProductsOfEnamelPinBadgesinCart(self):
        self.if_alert()
        element = self.driver.find_element_by_link_text("Stationery")
        action = ActionChains(self.driver)
        action.click(on_element = element)
        action.perform()
        Tees = self.driver.find_element_by_xpath(
            "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Stationery.Stationery_Name_EnamelPinBadges.value))
        Tees.click()
        for pins in EnamelPin:
            cloth = self.driver.find_element_by_xpath("//a[contains(text(),'%s')]" % str(pins.value))
            cloth.click()
            time.sleep(3)
            self.driver.find_element_by_xpath(
                "//div[@class='product-form__payment-container']//button[text()='Add to cart']").click()
            element = self.driver.find_element_by_link_text("Stationery")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            Tees = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Stationery.Stationery_Name_EnamelPinBadges.value))
            Tees.click()

    def addFoodAndDrinksInCart(self):
        self.if_alert()
        element = self.driver.find_element_by_link_text("Homeware")
        action = ActionChains(self.driver)
        action.click(on_element = element)
        action.perform()
        foods = self.driver.find_element_by_xpath(
            "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Homeware.Homeware_Name_Food_Drink.value))
        foods.click()
        for food in FoodAndDrinks:
            foodAndDrinks = self.driver.find_element_by_xpath("//a[contains(text(),'%s')]" % str(food.value))
            foodAndDrinks.click()
            time.sleep(3)
            self.driver.find_element_by_xpath(
                "//div[@class='product-form__payment-container']//button[text()='Add to cart']").click()
            element = self.driver.find_element_by_link_text("Homeware")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            foods = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Homeware.Homeware_Name_Food_Drink.value))
            foods.click()

    def addEmolyneItemsInCart(self):
        self.if_alert()
        element = self.driver.find_element_by_link_text("Beauty")
        action = ActionChains(self.driver)
        action.click(on_element = element)
        action.perform()
        foods = self.driver.find_element_by_xpath(
            "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Beauty.Beauty_Name_Emolyne.value))
        foods.click()
        for items in Emolyne:
            beautyItems = self.driver.find_element_by_xpath("//a[contains(text(),'%s')]" % str(items.value))
            beautyItems.click()
            time.sleep(3)
            self.driver.find_element_by_xpath(
                "//div[@class='product-form__payment-container']//button[text()='Add to cart']").click()
            element = self.driver.find_element_by_link_text("Beauty")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            foods = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Beauty.Beauty_Name_Emolyne.value))
            foods.click()


    



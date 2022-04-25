
# import os,sys
# myPath = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, myPath + '/../')

import time
import string
import random

from EnumsPackage.EnamelPinBadges import EnamelPinBadges
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
from EnumsPackage.VirtualGifts import VirtualGifts
from EnumsPackage.Emolyne import Emolyne

from EnumsPackage.TshirtsAndSweatShirts import TshirtsAndSweatShirts, TshirtsAndSweatShirtsAddedInCart

class HomePage(BasePage):
 
    def __init__(self, driver):
        super().__init__(driver)

    '''Title'''
    def get_home_page_title(self, title):
        return self.get_title(title)

    '''To check Cart icon'''
    def is_cart_icon_exist(self):
        return self.is_visible(Locators.CART_ICON)

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
            sorting.click()

    def clickHomeWareTab(self):
        for sorting in Homeware:
            element = self.driver.find_element_by_link_text("Homeware")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            sorting = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(sorting.value))
            sorting.click()

    def clickStationeryTab(self):
        for sorting in Stationery:
            element = self.driver.find_element_by_link_text("Stationery")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            sorting = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(sorting.value))
            sorting.click()

    def clickBeautyTab(self):
        for sorting in Beauty:
            element = self.driver.find_element_by_link_text("Beauty")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            sorting = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(sorting.value))
            sorting.click()
    
    def clickShopHomeTab(self):
        self.driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()
        self.driver.find_element_by_link_text("Shop Home")
        self.driver.find_element_by_xpath("(//a[@href='/collections/new-in'])[5]").click()
        print(self.driver.find_element_by_xpath(
            "24 //div[@class='product-item product-item--vertical  1/3--tablet-and-up 1/3--desk']")).size()

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
            self.driver.implicitly_wait(10)
            message = self.driver.find_element_by_xpath("//*[@id='star-message']").send_keys(
                ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10)))
            self.driver.find_element_by_xpath(
                "//div[@class='product-form__payment-container']//button[text()='Add to cart']").click()
            self.driver.find_element_by_link_text("Virtual Gifts").click()
        print(message)

    def clickSaleTab(self):
        self.driver.find_element_by_link_text("Sale")

    def clickOnCartButton(self):
        self.driver.find_element_by_xpath("//*[text()='Cart']").click()

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

    def addProductsOfEnamelPinBadgesinCart(self):
        self.driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()
        element = self.driver.find_element_by_link_text("Stationery")
        action = ActionChains(self.driver)
        action.click(on_element = element)
        action.perform()
        Tees = self.driver.find_element_by_xpath(
            "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Stationery.Stationery_Name_EnamelPinBadges.value))
        Tees.click()
        for pins in EnamelPinBadges:
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
        self.driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()
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
        self.driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()
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

    def is_items_exist_in_cart(self):
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
            self.driver.find_element_by_xpath(
                "//div[@class='product-form__payment-container']//button[text()='Add to cart']").click()
            element = self.driver.find_element_by_link_text("Clothing")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            Tees = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Clothing.CLOTHING_Name_TShirt.value))
            Tees.click()
        self.driver.find_element_by_xpath("//*[text()='Cart']").click()
        for getValue in TshirtsAndSweatShirtsAddedInCart:
            searchProductPresence  = self.driver.find_element_by_xpath(
                     "//a[contains(text(),'%s')]" % str(getValue.value))
        print(searchProductPresence.text)
        assert searchProductPresence.text == getValue.value
    



import time
from selenium.webdriver.common.action_chains import ActionChains
from EnumsPackage.EnamelPinBadges import EnamelPinBadges
from EnumsPackage.Stationery import Stationery
from Pages.BasePage import BasePage


class StationeryTab(BasePage):
     
    def __init__(self, driver):
        super().__init__(driver)

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
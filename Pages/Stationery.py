import time
from selenium.webdriver.common.action_chains import ActionChains
from EnumsPackage.EnamelPin import EnamelPin
from EnumsPackage.Stationery import Stationery
from Pages.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class StationeryTab(BasePage):
     
    def __init__(self, driver):
        super().__init__(driver)

    def addProductsOfEnamelPinBadgesinCart(self):
        self.driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()
        element = self.driver.find_element_by_link_text("Stationery")
        action = ActionChains(self.driver)
        action.click(on_element = element)
        action.perform()
        Enamel = self.driver.find_element_by_xpath(
            "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Stationery.Stationery_Name_EnamelPinBadges.value))
        Enamel.click()
        for pins in EnamelPin:
            # ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
            # your_element = WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions)\
            #             .until(EC.visibility_of_element_located(By.XPATH, "//a[contains(text(),'%s')]" )% str(pins.value))
            enamelPins = self.driver.find_element_by_xpath("//a[contains(text(),'%s')]" % str(pins.value))
            if(enamelPins.is_displayed()):
                enamelPins.click()
            else:
                raise Exception("no product available")
            print(enamelPins)
            enamelPins.click()
            time.sleep(3)
            self.driver.find_element_by_xpath(
                "//div[@class='product-form__payment-container']//button[text()='Add to cart']").click()
            element = self.driver.find_element_by_link_text("Stationery")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.perform()
            Enamel = self.driver.find_element_by_xpath(
                "//li[@class='nav-dropdown__item ']//a[contains(text(),'%s')]" % str(Stationery.Stationery_Name_EnamelPinBadges.value))
            Enamel.click()
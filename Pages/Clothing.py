import time
from EnumsPackage.Clothing import Clothing
from selenium.webdriver.common.action_chains import ActionChains
from EnumsPackage.TshirtsAndSweatShirts import TshirtsAndSweatShirts
from Pages.BasePage import BasePage

class ClothingTab(BasePage):
     
    def __init__(self, driver):
        super().__init__(driver)
        
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
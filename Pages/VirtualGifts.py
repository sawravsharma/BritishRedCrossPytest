import random
import string
import time
from Pages.BasePage import BasePage
from EnumsPackage.VirtualGifts import VirtualGifts


class VirtualGiftsTab(BasePage):
     
    def __init__(self, driver):
        super().__init__(driver)

    def addVirtualGiftsInCart(self):
        self.if_alert()
        self.driver.find_element_by_link_text("Virtual Gifts").click()
        time.sleep(5)
        for gift in VirtualGifts:
            giftEle = self.driver.find_element_by_xpath(
                "//span[contains(text(),'%s')]/following-sibling::a[contains(text(),'Send now')]" % str(gift.value))
            if(giftEle.is_displayed()):
                giftEle.click()
            else:
                raise Exception("no product available")
            print(gift)
            message = self.driver.find_element_by_xpath("//*[@id='star-message']").send_keys(
                ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10)))
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_xpath(
                "//div[@class='product-form__payment-container']//button[text()='Add to cart']").click()
            self.driver.find_element_by_link_text("Virtual Gifts").click()
        print(message)
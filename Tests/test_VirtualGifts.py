import pytest
from Pages.LoginPage import LoginPage
from Pages.VirtualGifts import VirtualGiftsTab
from Tests.test_Base import BaseTest


class Test_VirtualGifts(BaseTest):
    @pytest.mark.virtualgifts
    def test_addingVirtualGiftsInCart(self):
        self.loginPage = LoginPage(self.driver)
        virtualGift = VirtualGiftsTab(self.driver)
        virtualGift.addVirtualGiftsInCart()
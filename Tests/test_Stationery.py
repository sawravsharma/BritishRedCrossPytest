import pytest

from Pages.LoginPage import LoginPage
from Pages.Stationery import StationeryTab
from Tests.test_Base import BaseTest


class Test_StationeryTab(BaseTest):
    @pytest.mark.stationery
    def test_addingEnamelPinsInCart(self):
        self.loginPage = LoginPage(self.driver)
        enamel = StationeryTab(self.driver)
        enamel.addProductsOfEnamelPinBadgesinCart()
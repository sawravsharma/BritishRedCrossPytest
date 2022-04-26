import pytest
from Pages.HomeWare import HomewareTab
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest


class Test_HomeWare(BaseTest):
    @pytest.mark.foodDrinks
    def test_TshirtsAndSweatshirtstabs(self):
        self.loginPage = LoginPage(self.driver)
        homeWare = HomewareTab(self.driver)
        homeWare.addFoodAndDrinksInCart()
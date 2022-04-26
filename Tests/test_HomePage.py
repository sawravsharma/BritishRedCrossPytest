import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
import pytest
import allure 
from allure_commons.types import AttachmentType
from Tests.test_Base import BaseTest
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage

class Test_Home(BaseTest):

    # @pytest.mark.order(1)
    # def test_verify_dropdown_tabs(self):
    #     self.loginPage = LoginPage(self.driver)
    #     homePage  = HomePage(self.driver)
    #     homePage.is_items_exist_in_cart() /// add to cart page
    #     homePage.clickBeautyTab()
    #     homePage.clickNewInTab()
    #     homePage.clickTshirtsAndSweatShirtsTab()
    #     homePage.sortingProducts()
    #     homePage.clickVirtualGiftsTab()
    #     homePage.clickClothingTab()
    #     homePage.clickHomeWareTab()
    #     homePage.clickStationeryTab()
    #     homePage.clickShopHomeTab()
    #     homePage.clickVirtualGiftsTab()
    #     homePage.clickSaleTab()

    def test_click_on_addToCart_btn(self):
        self.loginPage = LoginPage(self.driver)
        homePage  = HomePage(self.driver)
        homePage.clickOnCartButton()

    def test_virtualgifts(self):
        self.loginPage = LoginPage(self.driver)
        homePage = HomePage(self.driver)
        homePage.clickVirtualGiftsTab()

    @pytest.mark.sort
    def test_sort_clothes(self):
        self.loginPage = LoginPage(self.driver)
        homePage = HomePage(self.driver)
        homePage.sortingProducts()

    @pytest.mark.homeware
    def test_verify_homeware_tab(self):
        self.loginPage = LoginPage(self.driver)
        homePage  = HomePage(self.driver)
        homePage.clickHomeWareTab()

    @pytest.mark.beauty
    def test_verify_beauty_tab(self):
        self.loginPage = LoginPage(self.driver)
        homePage  = HomePage(self.driver)
        homePage.clickBeautyTab()

    @pytest.mark.stationery
    def test_verify_stationery_tab(self):
        self.loginPage = LoginPage(self.driver)
        homePage  = HomePage(self.driver)
        homePage.clickStationeryTab()

    @pytest.mark.order()
    @pytest.mark.clothing
    def test_verify_clothing_tab(self):
        self.loginPage = LoginPage(self.driver)
        # loginPage = loginPage.do_login()
        homePage  = HomePage(self.driver)
        homePage.clickClothingTab()

    @pytest.mark.order
    @pytest.mark.shopHome
    def test_verify_Shop_Home_tab(self):
        self.loginPage = LoginPage(self.driver)
        homePage  = HomePage(self.driver)
        homePage.clickShopHomeTab()

    @pytest.mark.newIn
    @pytest.mark.order()
    def test_verify_New_In_tab(self):
        self.loginPage = LoginPage(self.driver)
        homePage  = HomePage(self.driver)
        homePage.clickNewInTab()


    @pytest.mark.sale
    @pytest.mark.order()
    def test_verify_Sale_tab(self):
        self.loginPage = LoginPage(self.driver)
        homePage  = HomePage(self.driver)
        homePage.clickSaleTab()

    
    '''Title'''
    @pytest.mark.order()
    def test_verify_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = HomePage(self.driver)
        title = homePage.get_title()
        assert title == TestData.HOME_PAGE_TITLE
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)
        print(title)

    '''Cart Icon'''
    @pytest.mark.order()
    def test_verify_cart_icon_visible(self):
        self.loginPage = LoginPage(self.driver)
        homePage  = HomePage(self.driver)
        cart_icon = homePage.is_cart_icon_exist()
        assert cart_icon 
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.JPG)








    # '''Sorting products in Low to High range'''
    # @pytest.mark.order(9)
    # def test_verify_sorting_L_to_H(self):
    #     self.loginPage = LoginPage(self.driver)
    #     homePage = self.loginPage.do_login()
    #     homePage.product_sort_container_low_to_high()
    #     allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    # '''Sorting products in High to Low range'''
    # @pytest.mark.order(10)
    # def test_verify_sorting_H_to_L(self):
    #     self.loginPage = LoginPage(self.driver)
    #     homePage = self.loginPage.do_login()
    #     homePage.product_sort_container_High_to_Low()
    #     allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    # '''Sorting products in Z to A name'''
    # @pytest.mark.order(11)
    # def test_verify_sorting_Z_To_A(self):
    #     self.loginPage = LoginPage(self.driver)
    #     homePage = self.loginPage.do_login()
    #     homePage.sort_products_by_Z_To_A()
    #     allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    # '''Sorting products in A to Z name'''
    # @pytest.mark.order(12)
    # def test_verify_sorting_A_To_Z(self):
    #     self.loginPage = LoginPage(self.driver)
    #     homePage = self.loginPage.do_login()
    #     homePage.sort_products_by_A_To_Z()
    #     allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

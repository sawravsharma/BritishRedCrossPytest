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

    def test_click_on_addToCart_btn(self):
        self.loginPage = LoginPage(self.driver)
        homePage  = HomePage(self.driver)
        homePage.clickOnCartButton()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    def test_virtualgifts(self):
        self.loginPage = LoginPage(self.driver)
        homePage = HomePage(self.driver)
        homePage.clickVirtualGiftsTab()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    @pytest.mark.sort
    def test_sort_clothes(self):
        self.loginPage = LoginPage(self.driver)
        homePage = HomePage(self.driver)
        homePage.sortingProducts()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    @pytest.mark.homeware
    def test_verify_homeware_tab(self):
        self.loginPage = LoginPage(self.driver)
        homePage  = HomePage(self.driver)
        homePage.clickHomeWareTab()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    @pytest.mark.beauty
    def test_verify_beauty_tab(self):
        self.loginPage = LoginPage(self.driver)
        homePage  = HomePage(self.driver)
        homePage.clickBeautyTab()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    @pytest.mark.stationery
    def test_verify_stationery_tab(self):
        self.loginPage = LoginPage(self.driver)
        homePage  = HomePage(self.driver)
        homePage.clickStationeryTab()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    @pytest.mark.order()
    @pytest.mark.clothing
    def test_verify_clothing_tab(self):
        self.loginPage = LoginPage(self.driver)
        homePage  = HomePage(self.driver)
        homePage.clickClothingTab()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    @pytest.mark.order
    @pytest.mark.shopHome
    def test_verify_Shop_Home_tab(self):
        self.loginPage = LoginPage(self.driver)
        homePage  = HomePage(self.driver)
        homePage.clickShopHomeTab()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    @pytest.mark.newIn
    @pytest.mark.order()
    def test_verify_New_In_tab(self):
        self.loginPage = LoginPage(self.driver)
        homePage  = HomePage(self.driver)
        homePage.clickNewInTab()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    @pytest.mark.sale
    @pytest.mark.order()
    def test_verify_Sale_tab(self):
        self.loginPage = LoginPage(self.driver)
        homePage  = HomePage(self.driver)
        homePage.clickSaleTab()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)
    
    '''Asserting Title'''
    @pytest.mark.order()
    def test_verify_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = HomePage(self.driver)
        title = homePage.get_title()
        assert title == TestData.HOME_PAGE_TITLE
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    '''Cart Icon exist or not'''
    @pytest.mark.order()
    def test_verify_cart_icon_visible(self):
        self.loginPage = LoginPage(self.driver)
        homePage  = HomePage(self.driver)
        cart_icon = homePage.is_cart_icon_exist()
        assert cart_icon 
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.JPG)

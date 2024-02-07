import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    # to get logger method from utility class
    logger = LogGen.loggen()

    # setup argument used from conftest file to avoid driver duplication
    def test_home_Page_Title(self, setup):
        self.logger.info("************** Test_001_Login *************")
        self.logger.info("************** Verifying Home Page Title *************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login5":
            assert True
            self.driver.close()
            self.logger.info("************** Home page Title test is passed *************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "home_Page_Title.png")
            self.driver.close()
            self.logger.error("************** Home page Title test is failed *************")
            assert False

    def test_login(self, setup):
        self.logger.info("************** Verifying login test *************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPasswords(self.password)
        self.lp.clickLogin()
        act_titles = self.driver.title

        if act_titles == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************** Login Test is passed *************")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("************** Login Test is failed *************")
            assert False

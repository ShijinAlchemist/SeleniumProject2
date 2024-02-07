import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import excelutils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    # username = ReadConfig.getUseremail()
    # password = ReadConfig.getPassword()
    # to get logger method from utility class
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("*****************Test_002_DDT_Login ****************")
        self.logger.info("************** Verifying login DDT test ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows=excelutils.getRowCount(self.path,'Sheet1')
        print("Number of rows in excel:",self.rows)
        lst_status=[]

        for r in range(2,self.rows+1):
            #read data from excel file
            self.user=excelutils.readData(self.path,'Sheet1',r,1)
            self.password=excelutils.readData(self.path,'Sheet1',r,2)
            self.exp=excelutils.readData(self.path,'Sheet1',r,3)

            self.lp.setUserName(self.user)
            self.lp.setPasswords(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="pass":
                    self.logger.info("****Passed****")
                    self.lp.clickLogout()
                    lst_status.append("pass")
                elif self.exp=="fail":
                    self.logger.info("*****failed******")
                    #self.lp.clickLogout()
                    lst_status.append("fail")

            elif act_title!=exp_title:
                if self.exp=="pass":
                    self.logger.info("****Failed****")
                    self.lp.clickLogout()
                    lst_status.append("fail")
                elif self.exp=="fail":
                    self.logger.info("*****passed******")
                    #self.lp.clickLogout()
                    lst_status.append("pass")

        if "fail" not in lst_status:
            self.logger.info("*******Login DDT test is Passed!********")
            self.driver.close()
            assert True


        else:
            self.logger.info("*******Login DDT test is Failed!*******")
            self.driver.close()
            assert False

        self.logger.info("*******End of DDT Test***********")
        self.logger.info("Complete Test_002_DDT_Login Test**********")





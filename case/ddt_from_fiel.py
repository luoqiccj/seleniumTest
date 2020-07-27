#coding:utf-8

#coding:utf-8
import ddt
import unittest
from business.login import loginBusiness
from selenium import webdriver
from utils.get_config import getConfig
import outcome
import  sys
import os
from utils.operate_excel import operateExcel

ex_data = operateExcel().get_excel_data()

@ddt.ddt
class loginddtcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        cfg = getConfig()
        self.driver = webdriver.Chrome()
        self.driver.get(getConfig().getconfig('url', 'login_url'))
        self.log_bus = loginBusiness(self.driver)

    @ddt.data(*ex_data)
    @ddt.unpack
    def test_login_case(self,username,password):
        print(username,password)
        self.log_bus.login(username,password)
        res = self.log_bus.get_error()
        self.assertFalse(res)

    def tearDown(self):
        print("self._testMethodName", self._testMethodName)
        self.driver.close()

if __name__ == '__main__':
    # unittest.main()
    suit = unittest.TestSuite()
    # suit.addTest(loginCase("test_login_success"))
    suit.addTest(loginddtcase("test_login_case"))
    unittest.TextTestRunner().run(suit)

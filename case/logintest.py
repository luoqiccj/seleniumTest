#coding:utf-8
from business.login import loginBusiness
from selenium import webdriver
import time

class logincase:
    def __init__(self,driver):
        self.log_bus = loginBusiness(driver)

    def test_login_success(self):
        self.log_bus.login("es_superadmin","123456")

    def test_login_usrname_error(self):
        self.log_bus.login_usrname_error("es_superadmi", "123456")

driver = webdriver.Chrome()
driver.get("http://192.168.0.37:8581/#/login")
logincase(driver).test_login_usrname_error()
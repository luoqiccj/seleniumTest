#coding:utf-8
from utils.get_config import getConfig
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

class findElement():
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,setion,option,filename=None):
        element = None
        cfg = getConfig(filename)
        data = cfg.getconfig(setion,option)
        by = data.split(">")[0]
        locater = data.split(">")[1]
        print(by,locater)
        try:
            locate = (By.XPATH, locater)
            re = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locate))

            if by == 'xpath':
                element = self.driver.find_element_by_xpath(locater)

            elif by == 'id':
                element = self.driver.find_element_by_id(locater)
            else:
                element = self.driver.find_element_by_xpath(locater)
        except:
            print("定位方式错误")

        return element

    def get_login_element(self,setion,filename=None):
        element = None

        cfg = getConfig(filename)
        data = cfg.getconfig("login_element",setion)
        by = data.split(">")[0]
        locater = data.split(">")[1]
        print(by,locater)
        try:
            locate = (By.XPATH, locater)
            re = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locate))

            if by == 'xpath':
                element = self.driver.find_element_by_xpath(locater)

            elif by == 'id':
                element = self.driver.find_element_by_id(locater)
            else:
                element = self.driver.find_element_by_xpath(locater)
        except:
            print("定位方式错误")

        return element

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://192.168.0.37:8581/#/login")
    findElement(driver).get_login_element('username')



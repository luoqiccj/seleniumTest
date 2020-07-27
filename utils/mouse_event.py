#coding:utf-8
from selenium.webdriver.common.action_chains import ActionChains as AC
from utils.find_element import findElement
from selenium import webdriver

class mouseEvent():
    def __init__(self,driver):
        self.driver = driver

    def click(self,element):
        AC(self.driver).click(element).perform()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://192.168.0.37:8581/#/login")




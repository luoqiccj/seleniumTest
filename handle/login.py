#coding:utf-8
from utils.find_element import findElement
from page.loginpage import loginPage
import selenium
from utils.mouse_event import mouseEvent
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class  loginHandle:
    def __init__(self,driver):
        self.driver = driver
        self.lg_page = loginPage(driver)
        self.mouseEvent = mouseEvent(driver)

    #输入用户名
    def send_usrname(self,data):
        element = self.lg_page.get_usrname_element().send_keys(data)
        #print("element",element)

    #输入密码
    def send_password(self,data):
        self.lg_page.get_password_element().send_keys(data)

    def logbtn_click(self):
        self.mouseEvent.click(self.lg_page.get_logbtn_element())

    def get_usr_error(self):
        return self.lg_page.get_usr_error_element()




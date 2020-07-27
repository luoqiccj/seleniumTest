#coding:utf-8
from utils.find_element import findElement

class loginPage():
    def __init__(self,driver ):
        self.element = findElement(driver)

    def get_usrname_element(self):
        element = self.element.get_element('login_element', 'username')
        #print("loginPage element",element)
        return element

    def get_password_element(self):
        element = self.element.get_element('login_element', 'password')
        return element

    def get_logbtn_element(self):
        element = self.element.get_element('login_element', 'loginbtn')
        return element

    def get_usr_error_element(self):
        element = self.element.get_element('login_element', 'usrname_error')
        print("get_usr_error_element element",element)
        return element

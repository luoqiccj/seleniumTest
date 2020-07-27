#coding:utf-8
from handle.login import loginHandle
import time

class loginBusiness:
    def __init__(self,driver):
        self.driver = driver
        self.lg_handle = loginHandle(driver)

    #执行操作
    def login(self,usrname,password):
        self.lg_handle.send_usrname(usrname)
        self.lg_handle.send_password(password)
        self.lg_handle.logbtn_click()

    def get_error(self):
        res = self.lg_handle.get_usr_error()
        return res

    def login_usrname_error(self,usrname,password):
        self.login(usrname,password)
        res = self.lg_handle.get_usr_error()
        return res

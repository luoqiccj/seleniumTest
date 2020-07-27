#coding:utf-8
from  selenium import webdriver
from utils.find_element import findElement
import time
class actionMethod:
    #打开浏览器
    def open_broswer(self,broswer):
        if broswer == 'ie':
            self.driver = webdriver.Edge()
        elif broswer == 'firebox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()
    #输入地址
    def get_url(self,url):
        self.driver.get(url)

    #定位元素
    def get_element(self,setion):
        find_elment = findElement(self.driver)
        element = find_elment.get_login_element(setion)
        return element

    #定位元素
    def get_expect_element(self,element):
        result = self.driver.find_element_by_xpath(element)
        return result

    #输入元素
    def element_send_keys(self,value,setion):
        print("setion",setion)
        element = self.get_element(setion)
        element.send_keys(value)

    #等待
    def sleep_time(self,times):
        time.sleep(times)

    #点击
    def element_click(self,setion):
        element = self.get_element(setion)
        element.click()

    #关闭浏览器
    def close_broswer(self):
        self.driver.close()





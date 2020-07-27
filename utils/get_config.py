#coding:utf-8
from configparser import ConfigParser
import string

class getConfig():
    #初始化
    def __init__(self,filename=None):
        if filename == None:
            self.filename = 'C:/Users/luoqi/PycharmProjects/seleniumTest/config/config.ini'
        else:
            self.filename = filename
        self.cfg = ConfigParser()

    #获取value值
    def getconfig(self,setion,option):
        self.cfg.read(self.filename)
        data = self.cfg.get(setion,option)
        return data


if __name__ == '__main__':
    res = getConfig().getconfig('element','username')
    print(res)





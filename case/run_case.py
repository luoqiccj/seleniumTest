#coding:utf-8

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
import os
import utils.HTMLTestRunner as HTMLTestRunner
import utils.Log

log = utils.Log.logger

class runCase(unittest.TestCase):
    def test_case01(self):
        file_path = os.path.join(os.path.dirname(os.getcwd()),"report","report.html")
        print(file_path)
        log.info(file_path)
        fd = open(file_path,"wb")

        path = os.path.join(os.getcwd())
        suit = unittest.defaultTestLoader.discover(path,"test_*.py")
        #unittest.TextTestRunner().run(suit)
        runner = HTMLTestRunner.HTMLTestRunner(stream=fd,title="Test case",description="dec")
        runner.run(suit)
        fd.close()


if __name__ == '__main__':
    unittest.main()

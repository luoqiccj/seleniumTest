#coding:utf-8
import xlrd
import os
import utils.Log
from xlutils.copy import copy

log = utils.Log.logger

class operateExcel:
    def __init__(self,filename = None,index = None):
        if filename==None:
            self.excel_path = os.path.join(os.path.dirname(os.getcwd()),"config","casedata.xls")
        else:
            self.excel_path = filename
        if index == None:
            index = 0

        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]

    #获取所有行数据
    def get_excel_data(self):
        data = []
        for i in range(1, self.get_lines()):
            rowdata = self.table.row_values(i)
            log.info(rowdata)
            data.append(rowdata)
        return data

    #获取行数
    def get_lines(self):
        nrows = self.table.nrows
        log.info(nrows)
        if nrows >= 1:
            return nrows
        else:
            return None


    #获取单元格内容
    def get_cell_data(self,row,col):
        data = self.table.cell(row,col).value
        log.info( data)
        return data

    #获取列数据
    def get_col_data(self,colx):
        data = self.table.col(colx)
        log.info(data)
        return data

    #写入数据
    def write_value(self,row,col,value):
        #read_data = self.data
        read_data = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_data)
        write_data.get_sheet(0).write(row,col,value)
        write_data.save(self.excel_path)


if __name__ == '__main__':
    operateExcel().get_excel_data()
    operateExcel().get_cell_data(1,1)
    operateExcel().get_col_data(1)
    operateExcel().write_value(3,3,1111)



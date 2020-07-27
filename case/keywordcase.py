#coding:utf-8
from utils.operate_excel import operateExcel
from keywords.action_method import actionMethod
import utils.Log
import os
import time
log = utils.Log.logger
is_run_col = 2
menthod_col =4
send_value_col =5
handle_value_col =6
expect_method_col = 7
expect_value_col = 8
result_col = 9

class keywordCase:
    def run_main(self):
        self.ac_methon = actionMethod()
        ex_path = os.path.join(os.path.dirname(os.getcwd()),"config","kw_casedata.xls")
        ex = operateExcel(ex_path)
        case_lines = ex.get_lines()
        if case_lines:
            for i in range(1,case_lines):
                #获取是否执行
                is_run = ex.get_cell_data(i,is_run_col)
                log.info("is_run = %s",is_run)
                if is_run == 'y':
                    method = ex.get_cell_data(i,menthod_col)
                    send_value = ex.get_cell_data(i, send_value_col)
                    handle_value = ex.get_cell_data(i, handle_value_col)
                    self.run_method(method,send_value,handle_value)
                    expect_method = ex.get_cell_data(i,expect_method_col)
                    log.info("expect_method=%s",expect_method)
                    expect_value = ex.get_cell_data(i,expect_value_col)
                    expect_value = self.get_expect_value(expect_value)
                    log.info("expect_value = %s",expect_value)
                    if expect_value != ['']:
                        if expect_value[0] == 'element':
                            res = self.run_method(expect_method,expect_value[1])
                            log.info("res =%s",res)
                            if res:
                                ex.write_value(i,result_col,"pass")
                            else:
                                ex.write_value(i, result_col,"fail")
                    else:
                        ex.write_value(i, result_col, "pass")
                        print("预期值为空")


    def get_expect_value(self,data):
        data = data.split('>')
        return data

    def run_method(self,method,send_value='',handle_value=''):
        method_value = getattr(self.ac_methon,method)
        log.info("send_value =%s",send_value)

        if send_value!='' and handle_value !='':
            log.info("handle_value =%s", handle_value)
            result = method_value(send_value,handle_value)
        elif send_value=='' and handle_value !='':
            result =method_value(handle_value)
        elif send_value!='' and handle_value =='':
            result =method_value(send_value)
        else:
            result =method_value()
        return result

if __name__ == '__main__':
    keywordCase().run_main()

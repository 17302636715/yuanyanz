#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import HTMLTestReportCN
import time
from DAY14.p2p_test.p2p.step4.libs.tools import (
     send_email,
     InsertLog,
     GetNewReport
)
# dirpath = './Scripts'
# discover = unittest.defaultTestLoader.discover(dirpath,pattern='*_tc.py')
# runner = unittest.TextTestRunner()
# runner.run(discover)
#执行测试 报告
def run_test():
    try:
        dirpath = './Scripts'
        discover = unittest.defaultTestLoader.discover(dirpath,pattern='test_*.py')
        currenttime = time.strftime('%y%m%d%H%M%S')
        filedir = './Reports/'+'report'+currenttime+'.html'
        with open(filedir,'wb') as f:
            runner = HTMLTestReportCN.HTMLTestRunner(
                stream = f,
                title = '计算器测试自动化测试报告',
                description = '计算机自动化测试详细内容',
                tester = '测试大神'
            )
            runner.run(discover)
        fire_report = GetNewReport('./Reports')
        send_email(s_user='yuanyan_z@163.com',s_pwd='yuan6270851',host='smtp.163.com',port=465,
                    to_user='ctyjqcq@163.com',body='老板，这是我的测试报告',subject='这是一封测试报告',report_file=fire_report)
    except BaseException as msg:
        log = InsertLog()
        log.error(msg)

if __name__ == '__main__':
    run_test()
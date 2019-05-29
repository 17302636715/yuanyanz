import requests
import unittest
import os
import yagmail
import logging


class HttpBase(object):
    localhost = 'http://localhost'

    def request_post(self, url, data, type=1, *args, **kwargs):
        urltest = '{}{}'.format(self.localhost, url)
        if type == 1:
            result = requests.post(url=urltest, data=data, *args, **kwargs)
        elif type == 2:
            result = requests.post(url=urltest, file=data, *args, **kwargs)
        return result

    def request_get(self, url, params, *args, **kwargs):
        urltest = '{}{}'.format(self.localhost, url)
        result = requests.get(url=urltest, params=params, *args, **kwargs)
        return result

    def request(self, method, url, data, *args, **kwargs):
        urltest = "{}{}".format(self.localhost, url)
        if method == 'post':
            result = requests.request('post', url=urltest, data=data, *args, **kwargs)
        elif method == 'get':
            result = requests.request('get', url=urltest, params=data, *args, **kwargs)

        return result


class VerifyClass(unittest.TestCase):
    def verifyCode(self,result,v_code):
        self.assertEqual(result.status_code,v_code)
    def verifyJson(self,result,key,value):
        result = result.json()
        v = result.get(key)
        self.assertEqual(v,value)
    def verifyHtml(self,result,value):
        result = result.text
        self.assertAlmostEquals(result,value)

cur_path = os.path.dirname(os.path.realpath(__file__))
# log_path是存放日志的路径
log_path = os.path.join(os.path.dirname(cur_path), 'log')
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path):
    os.mkdir(log_path)

class InsertLog():
    def __init__(self):
        # 文件的命名
        self.logname = os.path.join(log_path, '%s.log' %time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s - %(funcName)s line: %(lineno)3d] - %(levelname)s: %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a')  # 追加模式  这个是python2的
        # fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


def GetNewReport(FileDir):
    #打印目录所在所有文件名（列表对象）
    l = os.listdir(FileDir)
    l.sort(key=lambda fn:os.path.getmtime(FileDir + "\\" + fn))
    f = os.path.join(FileDir,l[-1])
    return f

# 发邮件
def send_email(s_user, s_pwd, host, port, to_user, body, subject, report_file):
    send = yagmail.SMTP(user=s_user,password=s_pwd,host=host,port=port)
    if type(to_user) is str:
        send.send(to=to_user,subject=subject,contents=[body,report_file])
        print('邮件发送成功')
    elif type(to_user) is list:
        send.send(to=to_user,cc=to_user,subject=subject,contents=[body,report_file])
        print('邮件发送成功')
    else:
        print('收件人信息错误')
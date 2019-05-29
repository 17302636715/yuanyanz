from DAY14.p2p_test.p2p.step4.libs.tools import HttpBase

class LoginBaseClass(HttpBase):
    Cookie = {
        'PHPSESSID':''
    }

    def login(self,email = 'test996',
              user_pwd = 'bXV1UE5Pb3BUeGd1RHpyY1RwdGpDSnpObFd2ZFFTZEJ4bXZ6T2NxUXlJWW90eU9sc0QlMjV1NjVCOSUyNXU3RUY0eXVhbjYyNzA4NTElMjV1OEY2RiUyNXU0RUY2',
              ajax = '1'):
        login_url = '/index.php?ctl=user&act=dologin'

        login_data = {
            'email': email,
            'user_pwd': user_pwd,
            'ajax': ajax
        }
        result = self.request('post', url=login_url, data=login_data)
        cookie = result.cookies['PHPSESSID']
        self.Cookie['PHPSESSID'] = cookie
        return result
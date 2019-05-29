from DAY14.p2p_test.p2p.step4.libs.basework import LoginBaseClass

class PrepayClass(LoginBaseClass):

    # 充值现金Api
    def prepayApi(self, check_ol_bl_pay='on', money='10000', pingzheng='',
                  memo='6222021411112222333', payment='5', bank_id='0'):
        url = '/member.php?ctl=uc_money&act=incharge_done'
        # 登录P2P后台
        self.login()
        data = {
            'check_ol_bl_pay': check_ol_bl_pay,
            'money': money,
            'pingzheng': pingzheng,
            'memo': memo,
            'payment': payment,
            'bank_id': bank_id,
        }
        # 充值线下支付
        result = self.request_post(url=url, data=data, cookies=self.Cookie)
        print(result.text)
        return result

if __name__ == '__main__':
    run = PrepayClass()
    result = run.prepayApi()
    print(result.status_code)


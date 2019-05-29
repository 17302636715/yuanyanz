from DAY14.p2p_test.p2p.step4.libs.basework import LoginBaseClass


class AddCard(LoginBaseClass):
    def add_card(self,real_name='amy',bank_id='36',otherbank='',region_lv1='1',region_lv2='6',region_lv3='77',
                 region_lv4='708',bankzone='%E5%A%9D%E5%AE%89%E6%94%AF%E8%A1%8C',bankcard = '6562+3789+0877+6666+6664',
                 reBankcard = '6562+3789+0877+6666+6664'):
        url = '/member.php?ctl=uc_money&act=savebank'
        self.login()
        data = {
            'real_name': real_name,
            'bank_id' : bank_id,
            'otherbank' : otherbank,
            'region_lv1' : region_lv1,
            'region_lv2' : region_lv2,
            'region_lv3' : region_lv3,
            'region_lv4' : region_lv4,
            'bankzone' : bankzone,
            'bankcard' : bankcard,
            'reBankcard' : reBankcard
        }

        result = self.request_post(url=url,data=data,cookies=self.Cookie)
        return result
if __name__ == '__main__':
    addcard = AddCard()
    result= addcard.add_card()
    print(result.status_code)

from DAY14.p2p_test.p2p.step4.libs.tools import VerifyClass
from DAY14.p2p_test.p2p.step4.po.MyP2P.CardList import AddCard
import unittest

class TestAddCardClass(VerifyClass):
    def setUp(self) -> None:
        self.a = AddCard()

    def test_add_card_success(self):
       result =  self.a.add_card()
       self.verifyCode(result,200)
       
if __name__ == '__main__':
    unittest.main()
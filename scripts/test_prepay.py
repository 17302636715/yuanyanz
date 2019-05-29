from DAY14.p2p_test.p2p.step4.po.MyP2P.PrepayCash import PrepayClass
import unittest
from DAY14.p2p_test.p2p.step4.libs.tools import VerifyClass

class TestPrepayApi(VerifyClass):
    def setUp(self) -> None:
        self.p = PrepayClass()
    def test_prepay_success(self):
        result = self.p.prepayApi()
        self.verifyCode(result,200)



if __name__ == '__main__':
    unittest.main()



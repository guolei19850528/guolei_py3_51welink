import unittest
from datetime import datetime

from guolei_py3_51welink.sms import SmsApi


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sms_api = SmsApi(
            base_url="https://api.51welink.com/",
            account_id="dljtwy00",
            password="g07KjuLN1",
            product_id=1012808
        )
        state = sms_api.send_sms("18242145566", f"测试短信{datetime.now().strftime('%Y%m%d%H%M%S')}【金泰物业】")
        if state:
            print("发送成功")
        self.assertTrue(state, "test failed")  # add assertion here


if __name__ == '__main__':
    unittest.main()

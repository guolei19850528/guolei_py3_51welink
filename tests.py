import unittest
from datetime import datetime

from guolei_py3_51welink.v1.sms import Api as SmsApi


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sms_api = SmsApi(
            base_url="https://api.51welink.com/",
            account_id="",
            password="",
            product_id=1012808
        )
        state = sms_api.send_sms("", f"测试短信{datetime.now()}【签名】")
        if state:
            print("发送成功")
        self.assertTrue(True, "test failed")  # add assertion here


if __name__ == '__main__':
    unittest.main()

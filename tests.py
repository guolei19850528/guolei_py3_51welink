import unittest
from datetime import datetime

from guolei_py3_51welink.sms import Api as SmsApi


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sms_api = SmsApi(
            base_url="https://api.51welink.com/",
            account_id="",
            password="",
            product_id=0
        )
        state = sms_api.send_sms("", f"")
        if state:
            print("发送成功")
        self.assertTrue(state, "test failed")  # add assertion here


if __name__ == '__main__':
    unittest.main()

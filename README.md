# guolei_py3_51welink

## introduce

**guolei python3 51welink library**

## software architecture

~python 3.*

## installation tutorial

```shell
pip install guolei-py3-51welink
```

## catalog description

### SmsApi example

```python
# @see https://www.lmobile.cn/ApiPages/index.html#page1
from guolei_py3_51welink.sms import Api as SmsApi

sms_api = SmsApi(
    base_url="https://api.51welink.com/",
    account_id="your accountId",
    password="your password",
    product_id="your productId"
)
state = sms_api.send_sms("手机号", "短信内容【签名】")
if state:
    print("发送成功")
```

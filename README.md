# guolei-py3-51welink

### a python3 library for 51welink

### [Document](https://www.lmobile.cn/ApiPages/index.html)

# Example

```python
from guolei_py3_51welink.library.sms import (
    Api as SmsApi, UrlSetting as SmsApiUrlSetting
)

sms_api: SmsApi = SmsApi(
    base_url="https://api.51welink.com/",
    account_id="<ACCOUNT ID>",
    password="<PASSWORD>",
    product_id="<PRODUCT ID>"
)

state: bool = sms_api.send_sms(
    path=SmsApiUrlSetting.ENCRYPTIONSUBMIT_SENDSMS,
    phone_nos="your phone number",
    content="your message conetnt【your sign】",
)
```
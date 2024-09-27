# guolei-py3-51welink
### a python3 library for 51welink

# Example
[官方文档](https://www.lmobile.cn/ApiPages/index.html)
```python
from guolei_py3_51welink.library.sms import (
    Api as SmsApi, ApiUrlSettings as SmsApiUrlSettings
)

sms_api = SmsApi(
    base_url="https://api.51welink.com/",
    account_id="<ACCOUNT ID>",
    password="<PASSWORD>",
    product_id="<PRODUCT ID>"
)

sms_send_state: bool = sms_api.post(
    url=SmsApiUrlSettings.URL__ENCRYPTIONSUBMIT_SENDSMS,
    kwargs={
        "json": {
            **sms_api.get_send_sms_data(
                data={
                    "PhoneNos": "your phone number",
                    "Content": "your message conetnt【your sign】"
                }
            )
        }
    }
)
```
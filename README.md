## 介绍

**微网通联 API**

[官方文档](https://www.lmobile.cn/ApiPages/index.html#page1)

## 软件架构

~python 3.*

## 安装教程

```shell
pip install guolei-py3-51welink
```

## 目录说明

### 短信 API 示例

```python
# @see https://www.lmobile.cn/ApiPages/index.html#page1
from guolei_py3_51welink.v1.sms import Api as SmsApi

sms_api = SmsApi(
    base_url="https://api.51welink.com/",
    account_id="your accountId",
    password="your password",
    product_id="your productId"
)
# 发送短信
state = sms_api.send_sms("手机号", "短信内容【签名】")
if state:
    print("发送成功")
```

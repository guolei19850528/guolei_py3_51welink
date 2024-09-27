#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
=================================================
作者：[郭磊]
手机：[15210720528]
Email：[174000902@qq.com]
Github：https://github.com/guolei19850528/guolei_py3_51welink
=================================================
"""

import hashlib
import random
import string
from datetime import time, datetime
from typing import Callable

import requests
from addict import Dict
from jsonschema.validators import validate, Draft202012Validator


class ApiUrlSettings:
    URL__ENCRYPTIONSUBMIT_SENDSMS = "/EncryptionSubmit/SendSms.ashx"


class Api(object):
    """
    微网通联短息API Class

    @see https://www.lmobile.cn/ApiPages/index.html
    """

    def __init__(
            self,
            base_url: str = "https://api.51welink.com/",
            account_id: str = "",
            password: str = "",
            product_id: int = 0,
            smms_encrypt_key: str = "SMmsEncryptKey",
    ):
        self._base_url = base_url
        self._account_id = account_id
        self._password = password
        self._product_id = product_id
        self._smms_encrypt_key = smms_encrypt_key

    @property
    def base_url(self):
        return self._base_url[:-1] if self._base_url.endswith("/") else self._base_url

    @base_url.setter
    def base_url(self, base_url):
        self._base_url = base_url

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        self._product_id = product_id

    @property
    def smms_encrypt_key(self):
        return self._smms_encrypt_key

    @smms_encrypt_key.setter
    def smms_encrypt_key(self, smms_encrypt_key):
        self._smms_encrypt_key = smms_encrypt_key

    def timestamp(self):
        return int(datetime.now().timestamp())

    def random_digits(self, length=10):
        return int("".join(random.sample(string.digits, length)))

    def password_md5(self):
        return hashlib.md5(f"{self.password}{self.smms_encrypt_key}".encode('utf-8')).hexdigest()

    def sha256_signature(self, data: dict = {}):
        data = Dict(data) if isinstance(data, dict) else Dict(data)
        temp = f"AccountId={data.AccountId}&PhoneNos={str(data.PhoneNos).split(",")[0]}&Password={self.password_md5().upper()}&Random={data.Random}&Timestamp={data.Timestamp}"
        return hashlib.sha256(temp.encode("utf-8")).hexdigest()

    def get_send_sms_data(self, data: dict = {}):
        data = Dict(data) if isinstance(data, dict) else Dict(data)
        data.setdefault("AccountId", self.account_id)
        data.setdefault("Timestamp", self.timestamp())
        data.setdefault("Random", self.random_digits())
        data.setdefault("ProductId", self.product_id)
        data.setdefault("PhoneNos", "")
        data.setdefault("Content", "")
        data.setdefault("AccessKey", self.sha256_signature(data))
        return data.to_dict()

    def post(
            self,
            url: str = "",
            params: dict = None,
            data: dict = None,
            kwargs: dict = None,
            custom_callable: Callable = None
    ):
        """
        use requests.post
        :param url: requests.post(url=url,params=params,data=data,**kwargs) url=base_url+url if not pattern ^http else url
        :param params: requests.post(url=url,params=params,data=data,**kwargs)
        :param data: requests.post(url=url,params=params,data=data,**kwargs)
        :param kwargs: requests.post(url=url,params=params,data=data,**kwargs)
        :param custom_callable: custom_callable(response) if isinstance(custom_callable,Callable)
        :return:custom_callable(response) if isinstance(custom_callable,Callable) else addict.Dict instance
        """
        if not Draft202012Validator({"type": "string", "minLength": 1, "pattern": "^http"}).is_valid(url):
            url = f"/{url}" if not url.startswith("/") else url
            url = f"{self.base_url}{url}"

        kwargs = Dict(kwargs) if isinstance(kwargs, dict) else Dict()
        response = requests.post(
            url=url,
            params=params,
            data=data,
            **kwargs.to_dict()
        )
        if isinstance(custom_callable, Callable):
            return custom_callable(response)
        if response.status_code == 200:
            print(response.json())
            json_addict = Dict(response.json())
            if Draft202012Validator({
                "type": "object",
                "properties": {
                    "Result": {
                        "type": "string",
                        "minLength": 1,
                        "const": "succ"
                    }
                },
                "required": ["Result"]
            }).is_valid(json_addict):
                return True
        return False

    def request(
            self,
            method: str = "GET",
            url: str = "",
            params: dict = None,
            data: dict = None,
            kwargs: dict = None,
            custom_callable: Callable = None
    ):
        """
        use requests.request
        :param method: requests.request(method=method,url=url,params=params,data=data,**kwargs)
        :param url: requests.request(method=method,url=url,params=params,data=data,**kwargs) url=base_url+url if not pattern ^http else url
        :param params: requests.request(method=method,url=url,params=params,data=data,**kwargs)
        :param data: requests.request(method=method,url=url,params=params,data=data,**kwargs)
        :param kwargs: requests.request(method=method,url=url,params=params,data=data,**kwargs)
        :param custom_callable: custom_callable(response) if isinstance(custom_callable,Callable)
        :return:custom_callable(response) if isinstance(custom_callable,Callable) else addict.Dict instance
        """
        if not Draft202012Validator({"type": "string", "minLength": 1, "pattern": "^http"}).is_valid(url):
            url = f"/{url}" if not url.startswith("/") else url
            url = f"{self.base_url}{url}"
        data = Dict(data) if isinstance(data, dict) else Dict()
        data.setdefault("token", self.token)
        data.setdefault("id", self.id)
        data.setdefault("version", self.version)
        kwargs = Dict(kwargs) if isinstance(kwargs, dict) else Dict()
        response = requests.request(
            method=method,
            url=url,
            params=params,
            data=data,
            **kwargs.to_dict()
        )
        if isinstance(custom_callable, Callable):
            return custom_callable(response)
        if response.status_code == 200:
            json_addict = Dict(response.json())
            if Draft202012Validator({
                "type": "object",
                "properties": {
                    "Result": {
                        "type": "string",
                        "minLength": 1,
                        "const": "succ"
                    }
                },
                "required": ["Result"]
            }).is_valid(json_addict):
                return True
        return False

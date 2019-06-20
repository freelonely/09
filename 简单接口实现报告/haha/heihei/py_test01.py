#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
from urllib.parse import urlencode
import requests
import unittest
from HTMLTestRunner import HTMLTestRunner
class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://apis.juhe.cn/simpleWeather/query"

    def test_weather_beijing(self):
        params = {"city": "北京"}
        key = {"key": "fccd435eed6999f9633bfeee0a78466e"}
        r = requests.get(self.url + "?city=" + params["city"] + "&key=" + key["key"])

        # print(r.json())
        # print(r.url)

        result = r.json()

        self.assertEqual(result["error_code"], 0)


# 请求地址
# base_url = "http://apis.juhe.cn/simpleWeather/query"

# 请求参数
# params = {"city":"北京"}
#
# key = {"key":"fccd435eed6999f9633bfeee0a78466e"}
# params = urllib.parse.urlencode(params)
# r = requests.get(base_url+ "?city=" + params["city"] + "&key=" + key["key"])
if __name__ == '__main__':
    unittest.main()


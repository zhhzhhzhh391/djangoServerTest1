# !/usr/bin/python3
# _*_coding:utf-8 _*_
""""
# @Time　　:2021/7/20
# @Author　 : zhuanghaha
# @File　　  :test_allure.py
# @Software  :PyCharm
# @blog     :https://blog.csdn.net/u010454117
# @WeChat Official Account: 【测试之路笔记】

#@allure.feature # 用于定义被测试的功能，被测产品的需求点
@allure.story # 用于定义被测功能的用户场景，即子功能点
with allure.step # 用于将一个测试用例，分成几个步骤在报告中输出
allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
@pytest.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤

"""
import pytest
import logging
import os
import allure
import requests

class TestEditionControlSystem():
    global host,headers
    host = "http://127.0.0.1:8000/wechat/api/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    @allure.feature("获取所有版本数据")
    def test_getAllEditionData(self):
        path = "getAllEditionData"
        """获取所有版本数据接口"""
        body = {
        }
        r = requests.request("GET",url=host+path,headers=headers,params=body)
        response = r.json()
        assert response["code"] == 20000
        logging.debug("获取到的code码 %",response['code'])

if __name__ == '__main__':
    pytest.main(['-s','-q','--alluredir','report/result','taskOne.py'])
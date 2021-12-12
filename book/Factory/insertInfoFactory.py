import abc
import logging
from book.models import User
import json
from django.core import serializers

class AbstractFactory(object):
    #抽象工厂  用来执行插入功能
    __metaclass__ = abc.ABCMeta
    @abc.abstractclassmethod
    def insert_user(self):
        pass

class insertUser(object):
    #插入操作
    def _insertListUser(userinfo):
        _userList = json.loads(userinfo)
        username = _userList.get('username')
        password = _userList.get('password')
        _userInsertObj = User(username=username,password=password)
        _userInsertObj.save()
        logging.debug("数据插入成功",_userInsertObj.username,_userInsertObj.password)





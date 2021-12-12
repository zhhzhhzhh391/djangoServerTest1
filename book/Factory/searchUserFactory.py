import abc
import logging
from book.models import User
import json
from django.core import serializers

class AbstractFactory(object):
    #抽象工厂
    __metaclass__ = abc.ABCMeta
    @abc.abstractclassmethod
    def search_user(self):
        pass
    def _searcObjecthUser(self):
        pass
    def _searchAllUser(self):
        pass
    def _searchAllUserUsername(self):
        pass

#指定搜索用
class searchUser(object):

    #用来搜索指定的账号
    def _searcObjecthUser(userInfo):
        _userListObject = json.loads(userInfo)
        logging.debug("工厂打印控制类传来的用户数据",_userListObject)
        logging.debug("登录请求的账号名称",_userListObject['username'])
        _userObject = User.objects.filter(username = _userListObject['username'])
        logging.debug("查询账号获得的账号数据",_userObject)
        return _userObject

    #用来获取所有的账号数据
    def _searchAllUser(self) -> object:
        _userListObject = User.objects.values()
        logging.debug("返回的所有用户的数据以及数据类型",_userListObject)
        # print("返回的用户的数据以及数据类型",type(_userListObject),_userListObject)
        return _userListObject

    #用来获取库内所有账号的username
    def _searchAllUserUsername(self):
        _userUsernameListObject = User.objects.all()
        logging.debug("返回的所有用户的用户名",_userUsernameListObject)
        return _userUsernameListObject

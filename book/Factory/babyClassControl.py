import abc
import logging
from book.models import FangTeacherClass
import json
from django.core import serializers

class AbstractFactory(object):
    #抽象工厂  用来执行插入功能
    __metaclass__ = abc.ABCMeta
    @classmethod
    def search_class(self):
        pass

    @classmethod
    def update_class(self):
        pass

    @classmethod
    def del_class(self):
        pass

class babyClassWork(object):
    def search_class(self,id):
        if id == None:
            _classContentList = FangTeacherClass.objects.all()
        else:
            _classContentList = FangTeacherClass.objects.filter(id=id)
        return _classContentList

    def update_class(classInfo):
        id = classInfo['id']
        try:
            if id:
                FangTeacherClass.objects.filter(id=classInfo['id']).update(**classInfo)
                return 1 #更新成功
            else:
                insertObj = FangTeacherClass(**classInfo)
                insertObj.save()
                return 2 #插入成功
            return 3
        except Exception as e:
            logging.error("插入方子音课程数据出错",e)
            return 3

    def del_class(classInfo):
        res = 0
        id = classInfo['id']
        delQueryData = FangTeacherClass.objects.filter(id=id)
        if delQueryData:
            delQueryData.delete()
            res = 1
        else:
            res = 2
        return res

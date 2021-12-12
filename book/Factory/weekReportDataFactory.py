import abc
import logging
from book.models import edition
from book.models import editionContent
import json
from django.core import serializers

class AbstractFactory(object):
    #抽象工厂
    __metaclass__ = abc.ABCMeta

    @classmethod
    def getSelectedData(self):
        pass

#更新周报数据用
class editionContentData(object):
    #获取所有周报数据
    def getSelectedData(self,editionContentId):
        _editionContentList = editionContent.objects.filter(editionType_id=editionContentId)
        logging.debug("获取版本所有内容数据")
        return _editionContentList

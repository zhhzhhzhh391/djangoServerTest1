import abc
import logging
from book.models import edition
from book.models import editionContent
import json
from django.core import serializers

class AbstractFactory(object):
    #抽象工厂
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def _insertEditionData(self):
        pass
    @abc.abstractclassmethod
    def _getAllEditionData(self):
        pass
    def _updateObjEditionData(self):
        pass
    def _getEditonData(self):
        pass
    def _getSelectedEditionData(self,id):
        pass
    def _delSelectedData(self,id):
        pass


#更新周报数据用
class updatetWeekReportData(object):
    #获取所有周报数据
    def _getEditonData(self,id):
        _editionContentList = editionContent.objects.filter(editionType_id=id)
        logging.debug("获取版本所有内容数据")
        return _editionContentList
    def _getSelectedEditionData(self,editionDict):
        id = editionDict['id']
        QAname = editionDict['QAname']
        functionName = editionDict['functionName']
        if id:
            _editionContent = editionContent.objects.filter(id=id)
        elif QAname and functionName == "":
            _editionContent = editionContent.objects.filter(author=QAname)
        elif QAname == "" and functionName:
            _editionContent = editionContent.objects.filter(functionName=functionName)
        elif QAname != "" and QAname and functionName != "" and functionName:
            _editionContent = editionContent.objects.filter(author=QAname,functionName=functionName)
        else:
            _editionContent = editionContent.objects.values()
        logging.debug("获取当前选择的版本数据内容")
        return _editionContent
    #插入全部周报数据
    def _insertEditionData(weekReportInfo):
        try:
            _editionContentInsertObj = editionContent(**weekReportInfo)
            _editionContentInsertObj.save()
            return 50001
        except Exception as e:
            logging.error("在创建版本数据的时候出现错误",e)

    #更新指定的版本内容数据
    def _updateObjEditionData(weekReportInfo):
        try:
            if weekReportInfo['id']:
                editionContent.objects.filter(id=weekReportInfo['id']).update(**weekReportInfo)
                return 1 #成功
            else:
                return 2 #未知错误
        except Exception as e:
            logging.error("版本内容更新时出现错误",e)
            return 3

    def _delSelectedEditionData(self,id):
        editionContent.objects.filter(id=id).delete()
        return 1

    def _delSelectEditionDataContentTypeId(self,editionContentId):
        editionContent.objects.filter(editionType_id=editionContentId).delete()
        logging.debug("使用contenttypeId删除数据成功")



#更新版本数据用
class updateEditionData(object):
    #插入版本相关的数据
    def _insertEditionData(editionInfo):
        try:
            _editionInsertObj = edition(**editionInfo)
            _editionInsertObj.save()
            return 50001
        except Exception as e:
            logging.error("在新建版本时出现异常",e.args)

    #获取所有版本的数据、避免插入重复名称
    def _getAllEditionData(self):
        _EditionDataList = edition.objects.values()
        logging.debug("返回的所有版本的数据", _EditionDataList)
        return _EditionDataList

    def _updateEditionData(self,id,editionDict):
        edition.objects.filter(id=id).update(**editionDict)
        return 50000 #成功

    def _getSelectedEditionData(self,id):
        _EditionDataList = edition.objects.filter(id=id)
        logging.debug("返回的版本数据和id",_EditionDataList,id)
        return _EditionDataList

    def _delSelectedData(self,id):
        edition.objects.filter(id=id).delete()
        logging.debug("版本数据删除成功")
        return 1




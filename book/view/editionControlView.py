from django.shortcuts import render
from book.models import User
from book.pojo import user
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from book.Factory import weekReportInfoFactory
import json
import traceback
import logging

#新增版本数据
@csrf_exempt
@require_http_methods("POST")
def insert_edition(request):
    response = {}
    try:
        _getEdition = request.body.decode('utf-8')
        _getEditionDict = json.loads(_getEdition)
        _edtionDataList = weekReportInfoFactory.updateEditionData._getAllEditionData(object)
        _getAllEditionName = list(_edtionDataList.filter().values('editionName'))  # 获取数据库所有用户的数据
        _getAllEditonContentId = list(_edtionDataList.filter().values('editionContentId')) #获取数据库所有用户的contentId
        if len(_getAllEditionName)==0:
            weekReportInfoFactory.updateEditionData._insertEditionData(_getEditionDict)
            response['code'] = 20001
            response['message'] = '版本数据插入成功'
        else:
            editionContentId = _getAllEditonContentId[len(_getAllEditonContentId)-1]['editionContentId'] + 1
            _getEditionDict['editionContentId'] = editionContentId
            weekReportInfoFactory.updateEditionData._insertEditionData(_getEditionDict)
            response['code'] = 20001
            response['message'] = '版本数据插入成功'
    except Exception as e:
        response['code'] = 40008 #新增版本出现错误
        response['message'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods("GET")
def get_edition(request):
    response = {}
    try:
        _getEdition = weekReportInfoFactory.updateEditionData._getAllEditionData()
        _getEditionList = list(_getEdition)
        response['code'] = 20000
        response['msg'] = _getEditionList
    except Exception as e:
        response['message'] = "获取版本数据的时候出错"
    return JsonResponse(response)

@csrf_exempt
@require_http_methods("POST")
def update_edition_data(request):
    response = {}
    try:
        getEdition = request.body.decode('utf-8')
        getEditionDict = json.loads(getEdition)
        id = getEditionDict['id']
        if id:
            res = weekReportInfoFactory.updateEditionData._updateEditionData(object,id,getEditionDict)
        elif id==None:
            getAllEdition = weekReportInfoFactory.updateEditionData._getAllEditionData(object)
            getAllEditionList = list(getAllEdition)
            lastContentId = getAllEditionList[len(getAllEditionList)-1]['editionContentId']
            getEditionDict['editionContentId'] = lastContentId + 1
            res = weekReportInfoFactory.updateEditionData._insertEditionData(getEditionDict)
        if res == 50000:
            response['code'] = 20001
            response['message'] = "更新版本数据成功"
            return JsonResponse(response)
        if res == 50001:
            response['code'] = 20001
            response['message'] = "插入新版本成功"
            return JsonResponse(response)
    except Exception as e:
        response['message'] = "更新版本数据出现错误"
        response['msg'] = str(e)
    return JsonResponse(response)

@csrf_exempt
@require_http_methods("POST")
def get_selected_edtition(request):
    response = {}
    try:
        getId = request.body.decode('utf-8')
        getIdDict = json.loads(getId)
        id = getIdDict['id']
        _getEdiiton = weekReportInfoFactory.updateEditionData._getSelectedEditionData(object,id)
        _getEdiitonList = list(_getEdiiton.values())
        response['code'] = 20000
        response['msg'] = _getEdiitonList
    except Exception as e:
        response['message'] = '获得指定版本数据出现错误'
    return JsonResponse(response)

@csrf_exempt
@require_http_methods("POST")
def del_selected_edition(request):
    response = {}
    try:
        getEdition = request.body.decode('utf-8')
        getEditionDict = json.loads(getEdition)
        editionContentId = getEditionDict['editionContentId']
        id = getEditionDict['id']
        print(editionContentId)
        weekReportInfoFactory.updateEditionData._delSelectedData(object,id)
        weekReportInfoFactory.updatetWeekReportData._delSelectEditionDataContentTypeId(object,editionContentId)
        response['code'] = 20001
        response['message'] = "删除版本成功"
    except Exception as e:
        response['code'] = 50000
        response['message'] = '删除指定版本出现错误'
        response['msg'] = str(e)
    return JsonResponse(response)
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
from django.core.cache import cache


#获取各个版本的数据
@require_http_methods("GET")
def get_all_edition_data(request):
    response = {}
    try:
        _edtionDataList = weekReportInfoFactory.updateEditionData._getAllEditionData(object)
        _getAllEditionDataList = list(_edtionDataList)
        response['code'] = 20000
        response['msg'] = _getAllEditionDataList
    except Exception as e:
        response['code'] = 20001 #新增版本出现错误
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@csrf_exempt
@require_http_methods("POST")
def insert_edition_content(request):
    response = {}
    try:
        _getEditionContent = request.body.decode('utf-8')
        _getEditionContent = json.loads(_getEditionContent)
        weekReportInfoFactory.updatetWeekReportData._insertEditionData(_getEditionContent)
        response['code'] = 20001
        response['msg'] = "更新版本内容数据成功"
    except Exception as e:
        response['code'] = 50008 #新增版本内容出现错误
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@csrf_exempt
@require_http_methods("POST")
def update_edition_content(request):
    response={}
    try:
        _getEditionContentList = request.body.decode('utf-8')
        _getEditionContentDict = json.loads(_getEditionContentList)
        id = _getEditionContentDict['id']
        res = 2
        if id:
            res = weekReportInfoFactory.updatetWeekReportData._updateObjEditionData(_getEditionContentDict)
        elif id == None:
            res = weekReportInfoFactory.updatetWeekReportData._insertEditionData(_getEditionContentDict)
        if res == 1:
            response['code'] = 20001 #更新版本内容成功
            response['message'] = "更新版本数据成功"
        elif res == 50001:
            response['code'] = 20001
            response['message'] = "插入新的版本数据成功"
        elif res == 2:
            response['code'] = 60001#未知错误
            response['message'] = "未知错误"
    except Exception as e:
        response['code'] = 60008  # 新增版本内容出现错误
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@csrf_exempt
@require_http_methods("POST")
def get_edition_content(request):
    response={}
    try:
        _getId = request.body.decode('utf-8')
        _id = json.loads(_getId)
        id = _id['id']
        _editionListObj = weekReportInfoFactory.updatetWeekReportData._getEditonData(object,id)
        _getAllEditionContent = list(_editionListObj.values())
        response['msg'] = _getAllEditionContent
        response['code'] = 20000
    except Exception as e:
        response['code'] = 70001
        response['msg'] = str(e)
    return JsonResponse(response)

@csrf_exempt
@require_http_methods("POST")
def get_selected_editon_content(request):
    response={}
    _getEditionData = request.body.decode('utf-8')
    _getEditionDataDict = json.loads(_getEditionData)
    try:
        _edtionContentObj = weekReportInfoFactory.updatetWeekReportData._getSelectedEditionData(object,_getEditionDataDict)
        editonContent = list(_edtionContentObj.values())
        response['msg'] = editonContent
        response['code'] = 20000
    except Exception as e:
        response['code'] = 80001
        response['msg'] = str(e)
    return JsonResponse(response)

@csrf_exempt
@require_http_methods("POST")
def del_selected_edition_content(request):
    response={}
    _getEditionContent = request.body.decode('utf-8')
    getEditionContentDict = json.loads(_getEditionContent)
    id = getEditionContentDict['id']
    try:
        res = weekReportInfoFactory.updatetWeekReportData._delSelectedEditionData(object,id)
        response['code'] = 30000
        response['message'] = "版本数据删除成功"
    except Exception as e:
        response['code'] = 20001
        response['msg'] = str(e)
    return JsonResponse(response)
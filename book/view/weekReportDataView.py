from django.shortcuts import render
from book.models import User
from book.pojo import user
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from book.Factory import weekReportDataFactory
from django.forms.models import model_to_dict
import json
import traceback
import logging

@csrf_exempt
@require_http_methods("POST")
def get_selectededition_bugNum(request):
    response={}
    try:
        selectedContentDict = {"QA":{},"bugNum":{},"caseNum":{}}
        _getEditionDataList = request.body.decode('utf-8')
        _getEditionDataDict = json.loads(_getEditionDataList)
        _getEdiitonContentId = _getEditionDataDict['editionContentId']
        _editionContent = weekReportDataFactory.editionContentData.getSelectedData(object,_getEdiitonContentId)
        _editionContentList= list(_editionContent.values())
        # for i in range(len(_editionContentList)):
        response['msg'] = _editionContentList
        response['code'] = 20000
        # 用map去管理当前版本每个人提交的bug数量
    except Exception as e:
        response['code'] = 20001 #新增版本出现错误
        response['message'] = "获取bug数量时出现错误"
        response['msg'] = str(e)
    return JsonResponse(response)
from django.shortcuts import render
from book.models import User
from book.pojo import user
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from book.Factory import babyClassControl
import json
import traceback
import logging

#新增版本数据
@csrf_exempt
@require_http_methods("POST")
def search_class(request):
    response = {}
    try:
        logging.debug("方紫音课表获取:")
        classContentObj = babyClassControl.babyClassWork.search_class(object,None)
        classContentList = list(classContentObj.values())
        response['msg'] = classContentList
        response['code'] = 20000
    except Exception as e:
        response['code'] = 20001 #查询课表报错
        response['msg'] = str(e)
    return JsonResponse(response)

@csrf_exempt
@require_http_methods("POST")
def update_class(request):
    response = {}
    try:
        logging.debug("方紫音课表更新")
        _getUpdateClass = request.body.decode('utf-8')
        _getUpdateClassDict = json.loads(_getUpdateClass)
        res = babyClassControl.babyClassWork.update_class(_getUpdateClassDict)
        if res == 1:
            response['code'] = 20000
            response['msg'] = "更新成功"
        elif res == 2:
            response['code'] = 20000
            response['msg'] = "插入成功"
    except Exception as e:
        response['code'] = 20002 #插入课表报错
        response['msg'] = str(e)
    return JsonResponse(response)

@csrf_exempt
@require_http_methods("POST")
def del_class(request):
    response = {}
    try:
        logging.debug("方紫音课表删除")
        _getDelClass = request.body.decode('utf-8')
        _getDelClassDict = json.loads(_getDelClass)
        res = babyClassControl.babyClassWork.del_class(_getDelClassDict)
        if res == 1:
            response['msg'] = "删除成功"
            response['code'] = 20000
        if res == 2:
            response['code'] = 20001
            response['msg'] = "删除出错"
        if res == 0:
            response['code'] = 20003
            response['masg'] = "未知错误"
    except Exception as e:
        response['code'] = 20003 #删除课表报错
        response['msg'] = str(e)
    return JsonResponse(response)



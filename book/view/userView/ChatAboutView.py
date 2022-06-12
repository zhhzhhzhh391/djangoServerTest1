from django.utils.datetime_safe import datetime
from rest_framework import status
import json
from book.models import ChatMsgData,User
from book.serializers import ClassControlUserSerializer,ChatMsgDataSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from book.constant import chatMsgCode
from django.core.paginator import Paginator
from rest_framework.response import Response

class ChatAboutViewSet(ModelViewSet):
    queryset = ChatMsgData.objects.all()
    serializer_class = ChatMsgDataSerializer

    user_queryset = User.objects.all()
    user_serializer_class = ClassControlUserSerializer

    @action(methods=['post'],detail=False)
    def getFriendObj(self,request):
        ret = {"code":0,"data":None}
        friendId = request.data.get('id',None)
        if id:
            friendObj = self.user_queryset.filter(id=friendId).first()
            ser = self.user_serializer_class(friendObj,many=False)
            ret['data'] = ser.data
            ret['code'] = chatMsgCode.GETFRIENDOBJ_SUCCESS
            return Response(data=ret,status=status.HTTP_200_OK)
        else:
            ret['code'] = chatMsgCode.GETFRIENDOBJ_FAIL
            return Response(data=ret,status=status.HTTP_200_OK)

    @action(methods=['post'],detail=False)
    def getChatMsgData(self,request):
        ret = {"code":0,"dataList":[]}
        groupName = request.data.get('groupName',None)
        page = request.data.get("page",None)
        if groupName and page:
            userObjList = []
            msgObjsList = self.queryset.filter(groupName=groupName).order_by('-id')#根据消息时间顺序降序排序
            paginator = Paginator(msgObjsList,10)
            if int(page)<=paginator.num_pages:
                msgObjs = paginator.page(page)
                for msgObj in msgObjs:
                    userObj = self.user_queryset.filter(id=msgObj.userId).first()
                    ser = self.serializer_class(msgObj,many=False,context={"nickname":userObj.nickname})
                    ret['dataList'].append(ser.data)
                ret['code'] = chatMsgCode.GETCHATMSGDATA_SUCCESS
                return Response(data=ret,status=status.HTTP_200_OK)
            else:
                ret['code'] = chatMsgCode.GETCHATMSGDATA_FULL
                return Response(data=ret,status=status.HTTP_200_OK)
        else:
            ret['code'] = chatMsgCode.GETCHATMSGDATA_FAILED
            return Response(data=ret,status=status.HTTP_200_OK)

from rest_framework import status

from book.models import ChatMsgData
from book.serializers import ClassControlUserSerializer,ChatMsgDataSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from book.constant import chatMsgCode
from django.core.paginator import Paginator
from rest_framework.response import Response

class ChatAboutViewSet(ModelViewSet):
    queryset = ChatMsgData.objects.all()
    serializer_class = ChatMsgDataSerializer

    @action(methods=['post'],detail=False)
    def getChatMsgData(self,request ):
        ret = {"code":0}
        groupName = request.data.get('groupName',None)
        page = request.data.get("page",None)
        if groupName and page:
            msgObjsList = self.queryset.filter(groupName=groupName).order_by('-id')#根据消息时间顺序降序排序
            paginator = Paginator(msgObjsList,5)
            msgObjs = paginator.page(page)
            ser = self.serializer_class(msgObjs,many=True)
            ret['code'] = chatMsgCode.GETCHATMSGDATA_SUCCESS
            ret['dataList'] = ser.data
            return Response(data=ret,status=status.HTTP_200_OK)
        else:
            ret['code'] = chatMsgCode.GETCHATMSGDATA_FAILED
            return Response(data=ret,status=status.HTTP_200_OK)

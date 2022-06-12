import logging

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from book.serializers import UserSettingSerializer
from book.models import User
from rest_framework.response import Response
from rest_framework import status
from book.constant import userSetting

class UserSettingAboutViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSettingSerializer

    @action(methods=['post'],detail=False)
    def getUserInfo(self,request):
        ret = {"code":userSetting.GETUSERINFO_FAIL,"data":None}
        id = request.data.get('id',None)
        user_obj = self.queryset.filter(id=id).first()
        ser = self.serializer_class(user_obj,many=False)
        ret['data'] = ser.data
        ret['code'] = userSetting.GETUSERINFO_SUCCESS
        if ser:
            return Response(data=ret,status=status.HTTP_200_OK)
    
    @action(methods=['post'],detail=False)
    def updateUserInfo(self,request):
        ret = {"code":userSetting.UPDATEUSERINFO_FAIL}
        id = request.data.get('id',None)
        user_obj = self.queryset.filter(id=id).first()
        ser = self.serializer_class(instance=user_obj,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            ret['code'] = userSetting.UPDATEUSERINFO_SUCCESS
            return Response(data=ret,status=status.HTTP_200_OK)
        else:
            return Response(data=ret,status=status.HTTP_200_OK)

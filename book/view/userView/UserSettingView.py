import logging

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from book.serializers import UserSettingSerializer
from book.models import User
from rest_framework.response import Response
from rest_framework import status

class UserSettingAboutViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSettingSerializer

    @action(methods=['post'],detail=False)
    def getUserInfo(self,request):
        id = request.data.get('id',None)
        user_obj = self.queryset.filter(id=id).first()
        ser = self.serializer_class(user_obj,many=False)
        if ser:
            return Response(data=ser.data,status=status.HTTP_200_OK)
    
    @action(methods=['post'],detail=False)
    def updateUserInfo(self,request):
        id = request.data.get('id',None)
        user_obj = self.queryset.filter(id=id).first()
        ser = self.serializer_class(instance=user_obj,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_200_OK)
        else:
            return Response(ser.errors)

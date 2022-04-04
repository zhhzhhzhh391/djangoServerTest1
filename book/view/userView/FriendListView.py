import json
import logging

from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from book.models import UserFriendList,User,FriendApply
from book.serializers import userFriendListSerializer,ClassControlUserSerializer,friendApplySerializer
from rest_framework import status
from book.constant import friendApplyCode

class FriendListViewSet(ModelViewSet):
    queryset = UserFriendList.objects.all()
    serializer_class = userFriendListSerializer

    user_queryset = User.objects.all()
    user_serializer_class = ClassControlUserSerializer
     #增加filter_fields属性

    #多对多查询
    @action(methods=['post'],detail=False)
    def getUserFriends(self,request):
        friendsInfoList = []
        userId = request.data.get('id',None)
        userFriends = self.queryset.filter(userId=userId)
        for friend in userFriends:
            friendObj = self.user_queryset.filter(id=friend.friendsId).first()
            friendsInfoList.append(friendObj)
        ser = self.user_serializer_class(friendsInfoList,many=True)
        if ser.data == None:
            return Response(data=ser.data,status=status.HTTP_200_OK)
        else:
            return Response(data=ser.data,status=status.HTTP_200_OK)


    @action(methods=['post'],detail=False)
    def getUserFriendsGroupName(self,request):
        userData = json.loads(request.data['user'])
        friendData = json.loads(request.data['friend'])
        if userData and friendData:
            friendListObj = self.queryset.filter(userId=userData.get('id'),friendsId=friendData.get('id')).first()
            ser = self.serializer_class(friendListObj,many=False)
        else:
            logging.ERROR("getUserFriendsGroupName无数据")
        return Response(data=ser.data,status=status.HTTP_200_OK)

class FriendApplyViewSet(ModelViewSet):
    queryset = FriendApply.objects.all()
    serializer_class = friendApplySerializer

    user_queryset = User.objects.all()
    user_serializer_class = ClassControlUserSerializer

    userList_queryset = UserFriendList.objects.all()
    userList_serializer_class = userFriendListSerializer

    @action(methods=['post'],detail=False)
    def getSelectUserApplyInfo(self,request):
        ret = {"code":0,"data":None,"dataList":None}
        ret["dataList"] = []
        applyFriendInfoList = []
        userId = request.data.get('id',None)
        applyFriendListObj = self.queryset.filter(friendsId=userId)
        try:
            for applyFriend in applyFriendListObj:
                dataObj = {}
                applyUserObj = self.user_queryset.filter(id=applyFriend.userId).first()
                ser1 = self.user_serializer_class(applyUserObj,many=False)
                applyStatus = self.queryset.filter(userId=applyFriend.userId).first()
                ser2 = self.serializer_class(applyStatus,many=False)
                dataObj = ser1.data
                dataObj['applyStatus'] = ser2.data.get("applyStatus")
                ret['dataList'].append(dataObj)
            ret['code'] = friendApplyCode.GETSELECTEDUSER_SUCCESS
        except:
            ret['code'] = friendApplyCode.GETSELECTEDUSER_FAILED

        # return Response(data=ser.data,status=status.HTTP_200_OK)
        return Response(data=ret,status=status.HTTP_200_OK)

    @action(methods=['post'],detail=False)
    def allowApply(self,request):
        ret = {"code":0}
        applyUser = json.loads(request.data['applyUser'])
        applyedUser = json.loads(request.data['applyedUser'])
        applyedUserId = applyedUser.get('id')
        applyUserId = applyUser.get('id')
        friendDataObj1 = self.userList_queryset.filter(userId=applyUserId,friendsId=applyedUserId).first()
        friendDataObj2 = self.userList_queryset.filter(userId=applyedUserId,friendsId=applyUserId).first()
        if friendDataObj1 and friendDataObj2 :
            ret = {"code":friendApplyCode.ADDFRIEND_FAILED}
            return Response(data=ret,status=status.HTTP_200_OK)
        else:
            #找不到好友表内这两个玩家的时候，就需要增加数据使得两个成为好友
            groupName = "zhuanghaha"+str(applyedUserId)+str(applyUserId)
            userListObj1 = UserFriendList.objects.create(userId=applyUserId,friendsId=applyedUserId,groupName=groupName)
            userListObj2 = UserFriendList.objects.create(userId=applyedUserId,friendsId=applyUserId,groupName=groupName)
            userListObj1.save()
            userListObj2.save()

            #更新申请表的状态
            applyFriendObj = self.queryset.filter(userId=applyUserId).first()
            updateFriendObj = self.queryset.filter(userId=applyUserId).first()
            updateFriendObj.applyStatus = 1

            ser = self.serializer_class(instance=applyFriendObj,data=model_to_dict(updateFriendObj),partial=True)
            if ser.is_valid():
                ser.save()
                ret = {"code":friendApplyCode.ADDFRIEND_SUCCESS,"data":ser.data}
                return Response(data=ret,status=status.HTTP_200_OK)
            else:
                return Response(data=ret,status=status.HTTP_200_OK)

    @action(methods=['post'],detail=False)
    def allowRefuse(self,request):
        ret = {"code":0}
        applyUser = json.loads(request.data['applyUser'])
        applyedUser = json.loads(request.data['applyedUser'])
        applyedUserId = applyedUser.get('id')
        applyUserId = applyUser.get('id')
        refuseFriendObj = self.queryset.filter(userId=applyUserId,friendsId=applyedUserId).first()
        saverefuseFriendObj = self.queryset.filter(userId=applyUserId,friendsId=applyedUserId).first()
        if refuseFriendObj:
            saverefuseFriendObj.applyStatus = 2
            ser = self.serializer_class(instance=refuseFriendObj,data=model_to_dict(saverefuseFriendObj),partial=True)
            if ser.is_valid():
                ser.save()
                ret = {"code":friendApplyCode.DELETFRIEND_SUCCESS,"data":ser.data}
                return Response(data=ret,status=status.HTTP_200_OK)
            else:
                ret = {"code":friendApplyCode.DELETFRIEND_FAILED}
                return Response(data=ret,status=status.HTTP_200_OK)
        else:
             ret = {"code":friendApplyCode.DELETFRIEND_FAILED}
             return Response(data=ret,status=status.HTTP_200_OK)

    @action(methods=['post'],detail=False)
    def addFriend(self,request):
        ret = {"code":0}
        applyUser = json.loads(request.data['applyUser'])
        applyedUser = json.loads(request.data['applyedUser'])
        applyedUserId = applyedUser.get('id')
        applyUserId = applyUser.get('id')
        addMsgObj = self.queryset.filter(userId=applyedUserId,friendsId=applyUserId).first()
        saveData = {}
        saveData['userId'] = applyedUserId
        saveData['friendsId'] = applyUserId
        saveData['applyStatus'] = 0
        if addMsgObj:
            ret={"code":friendApplyCode.APPLYSEND_EXIST}
            return Response(data=ret,status=status.HTTP_200_OK)
        else:
            ser = self.serializer_class(data=saveData)
            if ser.is_valid():
                ser.save()
                ret['code'] = friendApplyCode.APPLYSEND_SUCCESS
                return Response(data=ret,status=status.HTTP_200_OK)
            else:
                ret['code'] = friendApplyCode.APPLYSEND_FAILED
                return Response(data=ret,status=status.HTTP_200_OK)

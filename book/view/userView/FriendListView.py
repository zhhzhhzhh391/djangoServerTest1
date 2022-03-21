from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from book.models import UserFriendList,User
from book.serializers import userFriendListSerializer,ClassControlUserSerializer
from rest_framework import status

class FriendListViewSet(ModelViewSet):
    queryset = UserFriendList.objects.all()
    serializer_class = userFriendListSerializer

    user_queryset = User.objects.all()
    user_serializer_class = ClassControlUserSerializer


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

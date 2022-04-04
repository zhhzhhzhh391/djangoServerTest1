
import logging

from channels.exceptions import StopConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from book.constant import chatMsgCode
from book.models import User
from book.models import UserFriendList
from channels.db import database_sync_to_async

userList = [] #缓存当前房间用户信息
class UserListConsumer(AsyncWebsocketConsumer):

    async def websocket_connect(self,message):
        #连接后获取到房间的数据，进行分发
        #测试数据
        self.room_name = "zhh1"
        self.room_group_name = 'zhuanghaha' + self.room_name
        #用户连接后，进入房间组
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def websocket_disconnect(self,message):
        print("当前下线的用户为",message)
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    async def websocket_receive(self, text_data=None, bytes_data=None):
        #万一转的是json进行处理
        if type(text_data) == dict:
            text_data = json.dumps(text_data['text'])
            text_data_json = json.loads(json.loads(text_data))
            code = text_data_json['code']
            #用户上线
            if code == chatMsgCode.ENTERROOM_SUCCESS:
                #进入登录成功的逻辑
                userId = text_data_json['id']
                if userId not in userList:
                    userList.append(userId)
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type':'enterRoomDealer',
                        'id':userId,
                        'userList':userList,
                    }
                )

            #用户下线
            if code == chatMsgCode.LEAVEROOM_SUCCESS:
                userId = text_data_json['id']
                if userId in userList:
                    userList.remove(userId)
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type':'leaveRoomDealer',
                        'id':userId,
                        'userList':userList,
                    }
                )
                self.websocket_disconnect(userId)
                return

            #客户端发送消息处理code,进行分发处理
            if code == chatMsgCode.CHATMSG_SEND_SUCCESS:
                #处理聊天消息  客户端需要传送一个聊天内容和ID，用于存入redis
                msg = text_data_json['msg']
                id = text_data_json['id']
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type':'chatMsgDealer',
                        'msg':msg,
                        'id':id,
                    }
                )


    #用户成功进入房间，通知通道内所有用户有新用户进入
    #return :房间用户列表
    async def enterRoomDealer(self,event):
        id = event['id']
        userList = event['userList']
        await self.send(text_data=json.dumps({
            'code':chatMsgCode.ENTERROOM_SUCCESS,
            'data':{
                'id':id,
                'userList':userList,
            }
        }))

    #用户退出，通知状态给好友列表内其他玩家
    async def leaveRoomDealer(self,event):
        userList = event['userList']
        id = event['id']
        await self.send(text_data=json.dumps({
            'code':chatMsgCode.LEAVEROOM_SUCCESS,
            'data':{
                userList,
            }
        }))

    #某个用户发送新消息，通知通道内所有用户收到新消息
    async def chatMsgDealer(self,event):
        msg = event['msg']
        userId = event['id']
        nickname = await getUserNickName(object,userId)
        await self.send(text_data=json.dumps({
            'code':chatMsgCode.CHATMSG_RECEIVE_SUCCESS,
            'data':{
                nickname,
                msg,
                userId,
        }
        }))



@database_sync_to_async
def getUserNickName(self,userId):
    user_obj = User.objects.all().filter(id=userId).first()
    return user_obj.nickname

#返回当前用户的好友Id列表
@database_sync_to_async
def getUserFriendList(self,userId):
    friendIdList = []
    friendList = UserFriendList.objects.all().filter(userId=userId)
    for friend in friendList:
        friendIdList.append(friend.friendsId)
    return friendIdList


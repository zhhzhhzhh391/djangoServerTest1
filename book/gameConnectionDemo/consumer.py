from collections import UserDict
from email import message
import imp
import logging

from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from channels.layers import get_channel_layer
import json
from channels.exceptions import StopConsumer
from book.models import UserToken
from book.models import User
from book.constant import userCode,chatMsgCode
from book.models import User
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async

userList = [] #缓存当前房间用户信息
class ChatConsumer(AsyncWebsocketConsumer):

    async def websocket_connect(self,message):
        #连接后获取到房间的数据，进行分发
        #测试数据
        self.room_name = "zhh1"
        self.room_group_name = 'notice_%s' % self.room_name
        #用户连接后，进入房间组
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):  # 断开时触发
        
        # 将关闭的连接从群组中移除
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
            print(text_data)
            #新用户进入
            if code == chatMsgCode.ENTERROOM_SUCCESS:
                logging.info("账号登录成功，准备回调token")
                #进入登录成功的逻辑
                userId = text_data_json['id']
                if userId not in userList:
                    userList.append(userId)
                print(userList)
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type':'enterRoomDealer',
                        'userList':userList
                    }
                )

            #客户端发送消息处理code,进行分发处理
            if code == chatMsgCode.CHATMSG_SEND_SUCCESS:
                #处理聊天消息  客户端需要传送一个聊天内容和ID，用于存入redis
                msg = text_data_json['msg']
                userId = text_data_json['userId']
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type':'chatMsgDealer',
                        'msg':msg,
                        'userId':userId,
                    }
                )
    
    
    #用户成功进入房间，通知通道内所有用户有新用户进入
    #return :房间用户列表
    async def enterRoomDealer(self,event):
        userList = event['userList']
        await self.send(text_data=json.dumps({
            'code':chatMsgCode.ENTERROOM_SUCCESS,
            'msg':userList,
        }))

    #某个用户发送新消息，通知通道内所有用户收到新消息
    async def chatMsgDealer(self,event):
        msg = event['msg']
        userId = event['userId']
        nickname = await getUserNickName(object,userId)
        await self.send(text_data=json.dumps({
            'code':chatMsgCode.CHATMSG_SEND_SUCCESS,
            'nickname':nickname,
            'msg':msg,
            'userId':userId,
        }))

@database_sync_to_async
def getUserNickName(self,userId):
    user_obj = User.objects.all().filter(id=userId).first()
    return user_obj.nickname
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from book.constant import chatMsgCode
from book.models import User
from book.models import UserFriendList
from book.models import ChatMsgData
from channels.db import database_sync_to_async

 # self.userId = self.scope['url_route']['kwargs'].get("userId")

class chatConsumer(AsyncWebsocketConsumer):

    async def websocket_connect(self, message):
        return await super().websocket_connect(message)

    async def websocket_receive(self, text_data=None, bytes_data=None):
        #万一转的是json进行处理
        if type(text_data) == dict:
            text_data = json.dumps(text_data['text'])
            text_data_json = json.loads(json.loads(text_data))
            code = text_data_json['code']

            #聊天进入频道
            if code == chatMsgCode.CHAT_WITHOTHERS:
                userId = text_data_json['id']
                friendId = text_data_json['friendsId']
                group_name = await getChatGroupName(object,userId,friendId)
                print(group_name)
                await self.channel_layer.group_add(
                    group_name,
                    self.channel_name
                )

            if code == chatMsgCode.CHATMSG_SEND_SUCCESS:
                msg = text_data_json['msg']
                id = text_data_json['id']
                group_name = text_data_json['groupName']
                print(msg)
                await saveChatMsgData(object,id,msg,group_name)
                await self.channel_layer.group_send(
                    group_name,
                    {
                        'type':'chatMsgDealer',
                        'msg':msg,
                        'id':id,
                    }
                )
    async def chatMsgDealer(self,event):
        msg = event['msg']
        userId = event['id']
        userObj = await getUserInfo(object,userId)
        await self.send(text_data=json.dumps({
            'code':chatMsgCode.CHATMSG_RECEIVE_SUCCESS,
            'data':{
                'nickname':userObj.nickname,
                'msg':msg,
                'id':userId,
            }
        }))

    async def websocket_disconnect(self, message):
        return await super().websocket_disconnect(message)


@database_sync_to_async
def getChatGroupName(self,userId,friendId):
    friendObj = UserFriendList.objects.all().filter(userId=userId,friendsId=friendId).first()
    return friendObj.groupName

@database_sync_to_async
def getUserInfo(self,userId):
    user_obj = User.objects.all().filter(id=userId).first()
    return user_obj

@database_sync_to_async
def saveChatMsgData(self,userId,msg,groupName):
    ChatMsgData.objects.update_or_create(userId=userId,msg=msg,groupName=groupName)


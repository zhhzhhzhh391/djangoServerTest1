import logging

from channels.generic.websocket import WebsocketConsumer
import json
from channels.exceptions import StopConsumer
from book.models import UserToken
from book.models import User

userList = [] #缓存进入房间的用户信息

class ChatConsumer(WebsocketConsumer):

    def websocket_connect(self,message):
        self.accept()

    # def disconnect(self, code):
    #     pass

    def websocket_disconnect(self, message):
        raise StopConsumer

    def websocket_receive(self, text_data=None, bytes_data=None):
        #万一转的是json进行处理
        if type(text_data) == dict:
            text_data = json.dumps(text_data['text'])
            text_data_json = json.loads(json.loads(text_data))
            code = text_data_json['code']
            if code == 200:
                userId = text_data_json['id']
                username = text_data_json['username']
                print(username)
                token = UserToken.objects.filter(user_id=userId);
                msg = chat_code_to_msg(username,userId)
                self.send(text_data=json.dumps({
                    'code':200,
                    'msg':msg,
                }))
            else:
                self.send(text_data=json.dumps({
                'code':400,
                'msg':'erro',
            }))

#业务逻辑
def chat_code_to_msg(username,userId):
    user_item = {
        'id':userId,
        'username':username,
    }

    if user_item not in userList:
        userList.append(user_item)

    return userList

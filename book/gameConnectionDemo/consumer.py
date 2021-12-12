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
        print(text_data)
        #万一转的是json进行处理
        if type(text_data) == dict:
            text_data = json.dumps(text_data['text'])
        print(text_data)
        text_data_json = json.loads(json.loads(text_data))
        message = chat_code_to_msg(text_data_json['code'],text_data_json['msg'])

        self.send(text_data=json.dumps({
            'message':message
        }))


#业务逻辑
def chat_code_to_msg(code,msg):
    global userList

    if code == 100:
        pass

    res ={
        'code':100,
        'userList':msg
    }
    return res

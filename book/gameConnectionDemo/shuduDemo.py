import logging

from channels.generic.websocket import WebsocketConsumer
import json
from channels.exceptions import StopConsumer

#接收请求
class shuduConsumer(WebsocketConsumer):

    def websocket_connect(self,message):
        self.accept()


    def websocket_disconnect(self, message):
        raise StopConsumer

    def websocket_receive(self, text_data=None, bytes_data=None):
        #万一转的是json进行处理
        if type(text_data) == dict:
            text_data = json.dumps(text_data)

        text_data_json = json.loads(text_data)
        message = text_data_json['text']

        self.send(text_data=json.dumps({
            'shudumessage':message
        }))

#业务逻辑
def chat_code_to_msg(code,msg):
    if code == 100:
        pass

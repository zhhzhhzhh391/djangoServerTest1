import logging

from channels.generic.websocket import WebsocketConsumer
import json
from channels.exceptions import StopConsumer
from book.models import UserToken
from book.constant import userCode,chatMsgCode
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

            #给客户端回调token
            if code == userCode.USER_LOGIN_SUCCESS:
                logging.info("账号登录成功，准备回调token")
                #进入登录成功的逻辑
                userId = text_data_json['id']
                connectUserItem = getTokenFromServer(object,userId)
                self.send(text_data=json.dumps({
                    'code':200,
                    'msg':connectUserItem,
                }))

            #处理客户端发送的消息
            if code == chatMsgCode.CHATMSG_SUCCESS:
                #处理聊天消息  客户端需要传送一个聊天内容和ID，用于存入redis
                chatMsg = text_data_json['chatMsg']
                userId = text_data_json['userId']
                chatMsgDealer(object,chatMsg,userId)



#登录成功，返回token给客户端
def getTokenFromServer(self,userId):
    token_obj = UserToken.objects.filter(user_id=userId).first()
    user_obj = User.objects.filter(id=userId).first()
    if token_obj and user_obj:
        connectUserItem= {
        'id':user_obj.id,
        'username':user_obj.username,
        'token':token_obj.token,
        }
    return connectUserItem



#业务逻辑
def chatMsgDealer(self,chatMsg,userId):
    pass

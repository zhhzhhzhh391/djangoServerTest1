from book.gameConnectionDemo import consumer,chatConsumer
from django.urls import path,re_path

websocket_urlpatterns =[
    path('userListChannel', consumer.UserListConsumer.as_asgi()),
    # re_path('chatConsumer/(?P<userId>\w+)',chatConsumer.chatConsumer.as_asgi()),
    path('chatConsumer',chatConsumer.chatConsumer.as_asgi())
]

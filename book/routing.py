from book.gameConnectionDemo import shuduDemo, consumer
from django.urls import path

websocket_urlpatterns =[
    path('chatchannel', consumer.ChatConsumer.as_asgi()),
    path('shududemo',shuduDemo.shuduConsumer.as_asgi()),
]

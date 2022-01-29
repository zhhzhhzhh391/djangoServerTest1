from book.gameConnectionDemo import consumer
from django.urls import path

websocket_urlpatterns =[
    path('chatchannel', consumer.ChatConsumer.as_asgi()),
]

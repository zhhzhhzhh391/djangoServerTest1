from django.urls import path
from django.contrib import admin
from book.view import babyClassFormViewTest
# from book.view import websocketTestView
from rest_framework.routers import DefaultRouter
from book.view.userView import ClassControlUserView
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    #websocket测试
    # url(r'classAbout/$',view=babyClassFormViewTest.classListAPIView.as_view(),name="classList"),
    # url(r'classDetailAbout/(?P<pk>\d+)/$',view=babyClassFormViewTest.classDetailListAPIView.as_view(),name="classDetailList")
]

router = DefaultRouter() #创建路由
router.register(r'classAbout',babyClassFormViewTest.classInfoViewSet) #注册路由
router.register(r'UserAbout',ClassControlUserView.ClassControlUserViewSet)

urlpatterns += router.urls


"""
as_view() 内部定义了 view() 函数。view() 函数对类视图进行初始化，返回并调用了 dispatch() 方法。
dispatch() 根据请求类型的不同，调用不同的函数（如 get() 、 post()），并将这些函数的 response 响应结果返回。
as_view() 返回了这个 view 函数闭包，供 path() 路由调用
"""

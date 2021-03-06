
from rest_framework.routers import DefaultRouter
from book.view.userView import ClassControlUserView,UserSettingView,FriendListView,ChatAboutView

urlpatterns = [
    #websocket测试
    # url(r'classAbout/$',view=babyClassFormViewTest.classListAPIView.as_view(),name="classList"),
    # url(r'classDetailAbout/(?P<pk>\d+)/$',view=babyClassFormViewTest.classDetailListAPIView.as_view(),name="classDetailList")
]

router = DefaultRouter() #创建路由
router.register(r'UserAbout',ClassControlUserView.ClassControlUserViewSet)
router.register(r'UserSetting',UserSettingView.UserSettingAboutViewSet)#usersetting界面消息用
router.register(r'userFriendList',FriendListView.FriendListViewSet)#usersetting界面消息用
router.register(r'friendApply',FriendListView.FriendApplyViewSet)#friendapply界面消息用
router.register(r'ChatAbout',ChatAboutView.ChatAboutViewSet)

urlpatterns += router.urls


"""
as_view() 内部定义了 view() 函数。view() 函数对类视图进行初始化，返回并调用了 dispatch() 方法。
dispatch() 根据请求类型的不同，调用不同的函数（如 get() 、 post()），并将这些函数的 response 响应结果返回。
as_view() 返回了这个 view 函数闭包，供 path() 路由调用
"""

from django.urls import path, re_path

from django.conf.urls import url
from django.contrib import admin
from book.view import babyClassFormView,babyClassFormViewTest,weekReportDataView,editionControlView,weekReportView,classContentAboutView
# from book.view import websocketTestView
from rest_framework.routers import DefaultRouter
from book.view import ClassControlUserView
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('insertEdition',view=editionControlView.insert_edition,name="insertEdition"),
    path('insertEditionContent',view=weekReportView.insert_edition_content,name="insertEditionContent"),
    path('updateEditonContent',view=weekReportView.update_edition_content,name="updateEditionContent"),
    path('getEditionContent',view=weekReportView.get_edition_content,name="getEditonContent"),
    path('getSelectedEditionContent',view=weekReportView.get_selected_editon_content,name="getSelectedEditonContent"),
    path('getAllEditionData',view=weekReportView.get_all_edition_data,name="getAllEditionData"),
    path('updateEditionData',view=editionControlView.update_edition_data,name="updateEditionData"),
    path('getSelectedEditionData',view=editionControlView.get_selected_edtition,name="getSelectedEditionData"),
    path('delSelectedEditionContent',view=weekReportView.del_selected_edition_content,name="delSelectedEditionContent"),
    path('delSelectedEdition',view=editionControlView.del_selected_edition,name="delSelectedEdition"),
    path('getSelectedEditionBugNum',view=weekReportDataView.get_selectededition_bugNum,name="getSelectedEditionBugNum"),
    path('getClassContent',view=babyClassFormView.search_class,name="getClassContent"),
    path('updateClassContent',view=babyClassFormView.update_class,name="updateClassContent"),
    path('delClassContent',view=babyClassFormView.del_class,name="deleteClass"),

    #websocket测试

    # url(r'classAbout/$',view=babyClassFormViewTest.classListAPIView.as_view(),name="classList"),
    # url(r'classDetailAbout/(?P<pk>\d+)/$',view=babyClassFormViewTest.classDetailListAPIView.as_view(),name="classDetailList")
    url(r'^docs/',include_docs_urls(title="API site")),
    url(r'^admin/',admin.site.urls),

]

router = DefaultRouter() #创建路由
router.register(r'classAbout',babyClassFormViewTest.classInfoViewSet) #注册路由
router.register(r'UserAbout',ClassControlUserView.ClassControlUserViewSet)
router.register(r'ClassContentAbout',classContentAboutView.ClassContentAboutViewSet)

urlpatterns += router.urls


"""
as_view() 内部定义了 view() 函数。view() 函数对类视图进行初始化，返回并调用了 dispatch() 方法。
dispatch() 根据请求类型的不同，调用不同的函数（如 get() 、 post()），并将这些函数的 response 响应结果返回。
as_view() 返回了这个 view 函数闭包，供 path() 路由调用
"""

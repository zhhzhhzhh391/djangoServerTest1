
from book.models import FangTeacherClass
from book.serializers import FangTeacherClassSerializer
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.mixins import CreateModelMixin,ListModelMixin
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from book.pojo.pagination import LargerResultsSetPagination

class classInfoViewSet(ModelViewSet):
    serializer_class = FangTeacherClassSerializer
    queryset = FangTeacherClass.objects.all()

    # permission_classes = [IsAuthenticated]

    # pagination_class = LargerResultsSetPagination

    #查询最后一节课 classAbout/pk/latest/ get:latest
    #新增viewset方法，查询最新更新的一节课
    #detail = True 详情视图
    @action(methods=['get'],detail=False)
    def latest(self,request):
        """
        返回最后新更新的一节课
        :param request:
        :return:
        """
        classInfo = FangTeacherClass.objects.latest('id')
        serializer = self.get_serializer(classInfo)
        return Response(serializer.data)




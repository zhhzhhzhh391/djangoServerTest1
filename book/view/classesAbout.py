from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from book.models import FangTeacherClass
from book.serializers import FangTeacherClassSerializer
from rest_framework.viewsets import ModelViewSet

class classesAbout(ModelViewSet):
    queryset = FangTeacherClass.objects.all()
    serializer_class = FangTeacherClassSerializer

    @action(methods=['get'],detail=False)
    def getClasses(self,request):
        classesObj = self.queryset.all()
        ser = self.serializer_class(classesObj,many=True)
        return Response(data=ser.data,status=status.HTTP_200_OK)



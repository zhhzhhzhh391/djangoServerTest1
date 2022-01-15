
from book.models import ClassContentAbout
from book.serializers import ClassContentAboutSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class ClassContentAboutViewSet(ModelViewSet):
    queryset = ClassContentAbout.objects.all()
    serializer_class = ClassContentAboutSerializer

    @action(methods=['get'],detail=False)
    def getClassesName(self,request):
        classesname_obj = self.queryset.all()
        ser = self.serializer_class(classesname_obj,many=True)
        return Response(data=ser.data,status=status.HTTP_200_OK)







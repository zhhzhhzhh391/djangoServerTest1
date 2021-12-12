
from book.models import ClassContentAbout
from book.serializers import ClassContentAboutSerializer
from rest_framework.viewsets import ModelViewSet

class ClassContentAboutViewSet(ModelViewSet):
    queryset = ClassContentAbout.objects.all()
    serializer_class = ClassContentAboutSerializer



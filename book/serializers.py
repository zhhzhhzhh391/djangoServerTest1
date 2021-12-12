from rest_framework import serializers
from .models import FangTeacherClass
from .models import User
from .models import ClassContentAbout
from django.contrib.auth import get_user_model


class FangTeacherClassSerializer(serializers.ModelSerializer):

    classContentAbout = serializers.PrimaryKeyRelatedField(many=False,read_only=True)

    class Meta:
        model = FangTeacherClass
        fields = '__all__'

class ClassControlUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class ClassContentAboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassContentAbout
        fields = '__all__'

import imp
from operator import mod
from pyexpat import model
from tokenize import Token
from rest_framework import serializers
from .models import FangTeacherClass
from .models import User
from .models import UserToken
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

class userTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserToken
        fields = '__all__'

class ClassContentAboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassContentAbout
        fields = '__all__'

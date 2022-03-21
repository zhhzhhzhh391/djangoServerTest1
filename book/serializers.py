
from rest_framework import serializers
from .models import User
from .models import UserToken
from .models import ClassContentAbout
from .models import UserFriendList


class ClassControlUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class UserSettingSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class userTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserToken
        fields = '__all__'


class userFriendListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserFriendList
        fields = '__all__'

class ClassContentAboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassContentAbout
        fields = '__all__'

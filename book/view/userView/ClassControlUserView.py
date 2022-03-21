
import time
from datetime import datetime
from book.models import User
from book.models import UserToken
from book.serializers import ClassControlUserSerializer,userTokenSerializer
from rest_framework.authentication import BaseAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import exceptions
from rest_framework.response import Response
from book.pojo.JsonResponse import JsonResponse
from book.constant import userCode
from rest_framework import status
import hashlib


class ClassControlUserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ClassControlUserSerializer

    tokenQuerySet = UserToken.objects.all()
    token_serializer_class = userTokenSerializer

    @action(methods=['post'],detail=False)
    def getToken(self,request):
        """
        获取已经登陆的用户的token
        """
        id = request.data.get('id',None)
        username = request.data.get('username',None)
        user_obj = self.queryset.filter(username=username)
        user = user_obj.first()
        if username is None:
            tokendata = {}
            return Response(data=tokendata,
            status=status.HTTP_200_OK)
        if username:
            token_obj = self.tokenQuerySet.filter(user=user).first()
            ser = self.token_serializer_class(token_obj,many=False)
            return Response(data=ser.data,
            status=status.HTTP_200_OK)

    @action(methods=['post'],detail=False)
    def userlogin(self,request):
        """
        登录接口、获取登录用户信息
        :return:
        """
        username = request.data.get('username',None)
        password = request.data.get('password',None)
        if username and password is None:
            return JsonResponse(code=userCode.EMPTY_USERNAME_PASSWORD,
                                status=status.HTTP_200_OK,
                                msg=userCode.EMPTY_USERNAME_PASSWORD)
        user_obj = self.queryset.filter(username=username,password=password)
        user = user_obj.first()
        if user:
            #为用户创建token
            token = md5(user.username)
             # 保存(存在就更新不存在就创建，设置过期时间minutes=xx，xx时间表示多久过期)
            expiration_time = datetime.now()
            print(expiration_time, type(expiration_time))
            defaults = {
                "token": token,
                "expiration_time": expiration_time
            }
            UserToken.objects.update_or_create(user=user, defaults=defaults)
             #当对查询返回的QuerySet类型data进行反序列化的时候，如果传入的是多条数据，我们需要指定many=True
            ser = self.serializer_class(user,many=False)
            return Response(data=ser.data,
                            status=status.HTTP_200_OK)
        else:
            noUser = {}
            return Response(data=noUser,
                            status=status.HTTP_200_OK)



class TokenAuthtication(BaseAuthentication):
    def authenticate(self, request):
        # 1. 在请求头的query_params中获取token
        # token = request.query_params.get('token')
        # 2. 直接在请求头中获取token
        token = request._request.GET.get('token')
        token_obj = UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed("用户认证失败")
        else:
            datetime_now = datetime.now()
            if token_obj.expiration_time > datetime_now:
                # 在 rest framework 内部会将两个字段赋值给request，以供后续操作使用
                return (token_obj.user, token_obj)
            else:
                raise exceptions.AuthenticationFailed("用户tokepip install python-dateutiln过期,请重新登录")

    def authenticate_header(self, request):
        # 验证失败时，返回的响应头WWW-Authenticate对应的值
        pass

def md5(username):
    m = hashlib.md5(bytes(username, encoding='utf-8'))
    m.update(bytes(str(time.time()), encoding='utf-8'))
    return m.hexdigest()


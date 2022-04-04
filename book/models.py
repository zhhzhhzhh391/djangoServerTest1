from __future__ import unicode_literals
from django.db import models
from datetime import datetime

#用户数据表
class User(models.Model):
    username = models.CharField(max_length=64,verbose_name="用户名",help_text='用户名')
    password = models.CharField(max_length=64,verbose_name="密码")
    add_time = models.DateTimeField(auto_now_add=True,verbose_name="创建账号日期")
    email = models.CharField(max_length=64,verbose_name="邮箱")
    level = models.IntegerField(default="1",verbose_name="管理员等级")
    nickname = models.CharField(max_length=64,verbose_name="用户昵称",default="user")
    status = models.IntegerField(max_length=64,verbose_name="用户状态",default=0)#默认离线

    objects = models.Manager()

#存放用户token表
class UserToken(models.Model):
    user = models.OneToOneField(to="User",unique=True,on_delete=models.DO_NOTHING)
    token = models.CharField(max_length=64,verbose_name="用户token")
    expiration_time = models.DateTimeField(default=datetime.now,verbose_name="过期时间")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Mate:
        managed = True
        db_table = "user_token"
        verbose_name = "用户token"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.token
#用户的好友表
class UserFriendList(models.Model):
    userId = models.IntegerField(max_length=64,verbose_name="用户的ID")
    friendsId = models.IntegerField(max_length=64,verbose_name="对应的好友ID")
    groupName = models.CharField(max_length=254,verbose_name="好友频道名")

    class Mate:
        managed = True
        db_table = "userFriendList"
        verbose_name = "用户好友表"
        verbose_name_plural = verbose_name

    objects = models.Manager()

#好友申请列表
class FriendApply(models.Model):
    userId = models.IntegerField(max_length=64,verbose_name="申请人的Id")
    friendsId = models.IntegerField(max_length=64,verbose_name="被申请人的Id")
    applyStatus = models.IntegerField(max_length=64,verbose_name="申请状态")

    class Mate:
        manage = True
        db_table = "friendApply"
        verbose_name = "好友申请表"
        verbose_name_plural = verbose_name

    objects = models.Manager()

#聊天数据表
class ChatMsgData(models.Model):
    userId = models.IntegerField(max_length=64,verbose_name="发送消息的用户的ID")
    msg = models.CharField(max_length=254,verbose_name="聊天的内容")
    groupName = models.CharField(max_length=64,verbose_name="聊天组Id")
    msgTime = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Mate:
        manage = True
        db_table = "ChatMsgData"
        verbose_name = "聊天数据表"
        verbose_name_plural = verbose_name

    objects = models.Manager()


class ClassContentAbout(models.Model):
    artClass = models.CharField(max_length=64,verbose_name="课程名称")



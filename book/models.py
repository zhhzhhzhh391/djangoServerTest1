from __future__ import unicode_literals
from distutils.command.upload import upload
from pyexpat import model
from statistics import mode
from django.db import models
import datetime
from datetime import datetime
# Create your models here.

#用户数据表
class User(models.Model):
    username = models.CharField(max_length=64,verbose_name="用户名",help_text='用户名')
    password = models.CharField(max_length=64,verbose_name="密码")
    add_time = models.DateTimeField(auto_now_add=True,verbose_name="创建账号日期")
    email = models.CharField(max_length=64,verbose_name="邮箱")
    level = models.IntegerField(default="1",verbose_name="管理员等级")
    nickname = models.CharField(max_length=64,verbose_name="用户昵称",default="user")

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

class edition(models.Model):
    editionName = models.CharField(max_length=500,verbose_name="版本名称")
    projectName = models.CharField(max_length=500,verbose_name="项目名称")
    editionContentId = models.IntegerField(default='',verbose_name="对应版本内容id")
    weekReportDate = models.CharField(max_length=500,default='',verbose_name="当前版本日期")
    createDate = models.DateTimeField(auto_now=True,verbose_name="版本创建日期")

class editionContent(models.Model):
    functionName = models.CharField(max_length=500,verbose_name="功能点名称")
    functionComplete = models.CharField(max_length=500,verbose_name="功能完成度")
    caseNum = models.IntegerField(verbose_name="用例数量")
    bugNum = models.IntegerField(verbose_name="bug数量")
    fixBugNum = models.IntegerField(verbose_name="修复的bug数量")
    remark = models.CharField(max_length=500,verbose_name="备注")
    author = models.CharField(max_length=200,verbose_name="当前版本负责人",default='')
    editionType = models.ForeignKey('edition',on_delete=models.CASCADE,default='')
    casePercent = models.CharField(max_length=20,default='',verbose_name="用例进度")
    planTestTime = models.CharField(max_length=64,verbose_name="计划提测时间")
    realTestTime = models.CharField(max_length=64,verbose_name="实际测试时间")
    caseMakeSure = models.CharField(max_length=64,default='',verbose_name='用例核对')
    testedCaseNum = models.IntegerField(default=0,verbose_name="已测用例总数")
    passedCaseNum = models.IntegerField(default=0,verbose_name='通过用例总数')
    functionCompletePercent = models.CharField(max_length=255,default='',verbose_name="功能完成度")
    testProgress = models.CharField(max_length=255,default='',verbose_name="测试进度")
    bugBill = models.CharField(max_length=255,default='')

class FangTeacherClass(models.Model):
    # artClass = models.CharField(max_length=500,verbose_name="课程名称")
    classContent = models.ForeignKey('ClassContentAbout',on_delete=models.CASCADE)
    day = models.IntegerField( verbose_name="表示星期")
    dayNo = models.IntegerField(verbose_name="表示星期几的第几节课")
    personNum = models.IntegerField(verbose_name="上课人数")
    createDate = models.DateTimeField(auto_now=True,verbose_name="课程创建日期")

class ClassContentAbout(models.Model):
    artClass = models.CharField(max_length=64,verbose_name="课程名称")


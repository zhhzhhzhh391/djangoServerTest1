# Generated by Django 3.2.7 on 2021-10-26 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassContentAbout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artClass', models.CharField(max_length=64, verbose_name='课程名称')),
            ],
        ),
        migrations.CreateModel(
            name='edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editionName', models.CharField(max_length=500, verbose_name='版本名称')),
                ('projectName', models.CharField(max_length=500, verbose_name='项目名称')),
                ('editionContentId', models.IntegerField(default='', verbose_name='对应版本内容id')),
                ('weekReportDate', models.CharField(default='', max_length=500, verbose_name='当前版本日期')),
                ('createDate', models.DateTimeField(auto_now=True, verbose_name='版本创建日期')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='创建账号日期')),
                ('email', models.CharField(max_length=64, verbose_name='邮箱')),
                ('level', models.IntegerField(default='1', verbose_name='管理员等级')),
            ],
        ),
        migrations.CreateModel(
            name='FangTeacherClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(verbose_name='表示星期')),
                ('dayNo', models.IntegerField(verbose_name='表示星期几的第几节课')),
                ('personNum', models.IntegerField(verbose_name='上课人数')),
                ('createDate', models.DateTimeField(auto_now=True, verbose_name='课程创建日期')),
                ('classContent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.classcontentabout')),
            ],
        ),
        migrations.CreateModel(
            name='editionContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('functionName', models.CharField(max_length=500, verbose_name='功能点名称')),
                ('functionComplete', models.CharField(max_length=500, verbose_name='功能完成度')),
                ('caseNum', models.IntegerField(verbose_name='用例数量')),
                ('bugNum', models.IntegerField(verbose_name='bug数量')),
                ('fixBugNum', models.IntegerField(verbose_name='修复的bug数量')),
                ('remark', models.CharField(max_length=500, verbose_name='备注')),
                ('author', models.CharField(default='', max_length=200, verbose_name='当前版本负责人')),
                ('casePercent', models.CharField(default='', max_length=20, verbose_name='用例进度')),
                ('planTestTime', models.CharField(max_length=64, verbose_name='计划提测时间')),
                ('realTestTime', models.CharField(max_length=64, verbose_name='实际测试时间')),
                ('caseMakeSure', models.CharField(default='', max_length=64, verbose_name='用例核对')),
                ('testedCaseNum', models.IntegerField(default=0, verbose_name='已测用例总数')),
                ('passedCaseNum', models.IntegerField(default=0, verbose_name='通过用例总数')),
                ('functionCompletePercent', models.CharField(default='', max_length=255, verbose_name='功能完成度')),
                ('testProgress', models.CharField(default='', max_length=255, verbose_name='测试进度')),
                ('bugBill', models.CharField(default='', max_length=255)),
                ('editionType', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='book.edition')),
            ],
        ),
    ]
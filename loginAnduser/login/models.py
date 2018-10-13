from django.db import models
from django import forms

# Create your models here.


# 用户表
class UserInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    username = models.CharField(verbose_name='用户名', max_length=11)
    pwd = models.CharField(verbose_name='密码', max_length=12)


# 班级表
class ClassTable(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='班级名', max_length=32)


# student
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='姓名', max_length=22)
    class_id = models.OneToOneField(to='ClassTable', to_field='id', null=True, on_delete=models.CASCADE)


# teacher
class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='姓名', max_length=22)


# Class and Teacher
class TeacherClass(models.Model):
    id = models.AutoField(primary_key=True)
    teacher_id = models.OneToOneField(to='Teacher', to_field='id', null=True, on_delete=models.CASCADE)
    class_id = models.OneToOneField(to='ClassTable', to_field='id', null=True, on_delete=models.CASCADE)


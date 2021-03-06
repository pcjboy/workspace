# Generated by Django 2.1.2 on 2018-10-14 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, verbose_name='班级名')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=22, verbose_name='姓名')),
                ('class_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.ClassTable')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=22, verbose_name='姓名')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherClass',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('class_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.ClassTable')),
                ('teacher_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=11, verbose_name='用户名')),
                ('pwd', models.CharField(max_length=12, verbose_name='密码')),
            ],
        ),
    ]

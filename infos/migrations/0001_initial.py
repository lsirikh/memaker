# Generated by Django 2.1.2 on 2019-06-09 10:55

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='제목')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(max_length=8000, verbose_name='본문 내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록 날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='업데이트 날짜')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='제목')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(max_length=8000, verbose_name='본문 내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록 날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='업데이트 날짜')),
            ],
        ),
    ]

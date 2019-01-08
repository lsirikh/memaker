# Generated by Django 2.1.2 on 2019-01-01 15:13

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0021_remove_lecture_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appraisal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=5, verbose_name='평가등급')),
                ('message', models.TextField(max_length=500, verbose_name='내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록 날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='업데이트 날짜')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Content')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduce', ckeditor_uploader.fields.RichTextUploadingField(max_length=6000, verbose_name='내용')),
                ('link', models.URLField(blank=True, default='', verbose_name='구매링크')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Content')),
            ],
        ),
        migrations.CreateModel(
            name='ReplyChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', ckeditor_uploader.fields.RichTextUploadingField(max_length=3000, verbose_name='내용')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='순서')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록 날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='업데이트 날짜')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='no title', max_length=200, verbose_name='제목')),
                ('video_link', models.URLField(blank=True, verbose_name='강의영상')),
                ('introduce', models.TextField(blank=True, max_length=3000, verbose_name='내용')),
            ],
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='location',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='period_from',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='period_to',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='register_from',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='register_to',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='teacher',
        ),
        migrations.AddField(
            model_name='video',
            name='lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Lecture'),
        ),
        migrations.AddField(
            model_name='replychapter',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Video'),
        ),
    ]

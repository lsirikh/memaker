from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


class Board(models.Model):
    name = models.CharField('게시판', max_length=30, unique=True)
    description = models.CharField('게시판 설명', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_topics_count(self):
        return Topic.objects.filter(topic__board=self).count()

    def get_last_topic(self):
        return Topic.objects.filter(topic__board=self).order_by('-updated_at', '-created_at')



class Topic(models.Model):
    title = models.CharField('제목', max_length=255)
    user = models.ForeignKey(User, related_name='topic', on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name='topic', on_delete=models.CASCADE)

    message = RichTextUploadingField('본문 내용', max_length=4000)
    created_at = models.DateTimeField('등록 날짜', auto_now_add=True, blank=True)
    updated_at = models.DateTimeField('업데이트 날짜', blank=True)
    views = models.PositiveIntegerField('조회수', default=0)

    def __str__(self):
        return self.title




class Post(models.Model):
    #message = RichTextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)

    message = RichTextUploadingField('본문 내용', max_length=4000)
    order = models.PositiveIntegerField('순서', default=0)
    created_at = models.DateTimeField('등록 날짜', auto_now_add=True, blank=True)
    updated_at = models.DateTimeField('업데이트 날짜', auto_now=True, blank=True)
    is_post_to_post = models.BooleanField('대댓글 여부', blank=True, default=False)
    post_to_post_address = models.PositiveIntegerField('대상댓글', blank=True, null=True)

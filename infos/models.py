from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class ServiceUsage(models.Model):
    title = models.CharField('제목', max_length=255)
    content = RichTextUploadingField('본문 내용', )
    created_at = models.DateTimeField('등록 날짜', auto_now_add=True, blank=True)
    updated_at = models.DateTimeField('업데이트 날짜', auto_now=True, blank=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('infos:board_topic', args=[self.pk])

class PrivacyPolicy(models.Model):
    title = models.CharField('제목', max_length=255)
    content = RichTextUploadingField('본문 내용',)
    created_at = models.DateTimeField('등록 날짜', auto_now_add=True, blank=True)
    updated_at = models.DateTimeField('업데이트 날짜', auto_now=True, blank=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('infos:board_topic', args=[self.pk])
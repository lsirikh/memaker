from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_topics_count(self):
        return Topic.objects.filter(topic__board=self).count()

    def get_last_topic(self):
        return Topic.objects.filter(topic__board=self).order_by('-updated_at', '-created_at')



class Topic(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='topic', on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name='topic', on_delete=models.CASCADE)
    message = RichTextUploadingField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title




class Post(models.Model):
    #message = RichTextField(max_length=4000)
    message = RichTextUploadingField(max_length=4000)
    order = models.PositiveIntegerField(default=0)
    topic = models.ForeignKey(Topic, related_name='post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    user = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
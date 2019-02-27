from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail
from ckeditor_uploader.fields import RichTextUploadingField

from django.db.models.signals import pre_save
from django.urls import reverse
from memaker.utils import unique_slug_generator

import os

# Create your models here.

class Category(models.Model):
    title = models.CharField('제목', max_length=200, db_index=True, default='no title') # 제목
    section = models.CharField('구분', max_length=200, db_index=True, default='') # 구분 ex) 강의, 상품

    #slug 추가
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True) #Slug field add


    description = models.CharField('설명', max_length=100, null=True, blank=True) # 간략 설명

    def __str__(self):
        return '{0}-{1}'.format(self.title, self.section)

    def get_absolute_url(self):
        return reverse('products:content_category_list',
                       args=[self.slug])

    class Meta:
        ordering = ('section',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class Image(models.Model):
    #content = models.ManyToManyField('products.Content') # Content와 ManyToMany 설정

    image = models.ImageField('샘플이미지', upload_to='content_image/%Y/%m/%d', blank=True)  # 이미지
    thumbnail = ImageSpecField(  # 이미지 썸네일
        source='image',
        processors=[Thumbnail(600, 400)],
        format='JPEG',
        options={'quality': 80})
    description = models.CharField('사진설명', null=True, blank=True, max_length=100) # 간략한 이미지 설명

    def __str__(self):
        return self.description

class File(models.Model):
    #content = models.ManyToManyField('products.Content')  # Content와 ManyToMany 설정

    file = models.FileField('파일', upload_to='content_file/%Y/%m/%d', null=True, blank=True)
    description = models.CharField('파일설명', null=True, blank=True, max_length=100)  # 간략한 파일 설명
    type = models.CharField('확장자', max_length=10, null=True, blank=True)

    def __str__(self):
        return self.description




class Content(models.Model):
    RECOMMEND_CHOICE = (
        (1, '인기'),
        (2, '추천'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE) # 카테고리
    related_content = models.ManyToManyField('products.Content', blank=True) # 관련콘텐츠

    title = models.CharField('제목', max_length=200, default='no title', db_index=True)  # 제목

    # slug 추가
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True, db_index=True)  # Slug field add

    added = models.DateTimeField('등록 날짜', auto_now_add=True, blank=True)  # 등록한 날짜
    updated = models.DateTimeField('업데이트 날짜', auto_now=True, blank=True)  # 업데이트 날짜
    description = models.CharField('간략설명', null=True, blank=True, max_length=300)  # 간략한 설명
    sample = models.URLField('샘플영상', null=True, blank=True)  # 샘플영상

    cost = models.PositiveIntegerField('정가', null=True, blank=True, default=0)  # 가격
    discount = models.PositiveIntegerField('할인가격', null=True, blank=True, default=0)  # 할인 가격

    isSale = models.BooleanField('판매여부', null=True, blank=True, default=False)  # 판매 여부
    isShow = models.BooleanField('노출여부', null=True, blank=True, default=False) #노출여부
    isDiscount = models.BooleanField('할인', null=True, blank=True, default=False) #할인여부
    recommend = models.IntegerField('추천', choices=RECOMMEND_CHOICE, null=True, blank=True) #추천여부

    image = models.ManyToManyField(Image, blank=True)
    file = models.ManyToManyField(File, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:content_information',
                       args=[self.slug])

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)





def slug_save(sender, instance, *args, **kwargs):
    if not instance:
        instance.slug = unique_slug_generator(instance, instance.title, instance.slug)

pre_save.connect(slug_save, sender=Category)



class Lecture(models.Model):

    content = models.ForeignKey(Content, on_delete=models.CASCADE) # Content와 ForeignKey 설정
    teacher = models.ManyToManyField(User, blank=True)

    #############################Lecture attribute###########################
    introduce = RichTextUploadingField('내용', max_length=8000)
    register_from = models.DateField('등록일', blank=True, null=True)
    period_from = models.DateField('시작일', blank=True, null=True)
    period_to = models.DateField('종료일', blank=True, null=True)
    duration = models.DurationField('기간', blank=True, null=True)
    location = models.CharField('교육장소', max_length=300, blank=True)
    #########################################################################

    def __str__(self):
        return '{0}-lecture({1})'.format(self.content, self.pk)

class Video(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE) # Lecture와 ForeignKey 설정

    title = models.CharField('제목', max_length=200, default='no title')  # 제목
    video_link = models.URLField('강의영상', blank=True) # 영상링크
    introduce = RichTextUploadingField('내용', max_length=3000, blank=True) # 내용

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id',)

class Product(models.Model):

    content = models.ForeignKey(Content, on_delete=models.CASCADE)  # Content와 ForeignKey 설정
    introduce = RichTextUploadingField('내용', max_length=8000) # 내용
    link = models.URLField('구매링크', default='', blank=True) # 네이버 구매 링크

    stock = models.PositiveSmallIntegerField('재고', default=0) #제고 물건만 유의미


    def __str__(self):
        return '{0}-product({1})'.format(self.content, self.pk)


################################################################################################
class Appraisal(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE) # Content와 ForeignKey 설정
    user = models.ForeignKey(User, on_delete=models.CASCADE) # User 와 ForeignKey 설정

    rate = models.IntegerField('평가등급', default=5, null=False, blank=False) # 평가등급
    message = models.TextField('내용', max_length=500) # 내용

    created_at = models.DateTimeField('등록 날짜', auto_now_add=True, blank=True) # 등록 날짜
    updated_at = models.DateTimeField('업데이트 날짜', auto_now=True, blank=True) # 업데이트 날짜

    def __str__(self):
        return '{0}-Appraisal({1})'.format(self.content, self.pk)


class ReplyChapter(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE) # Video 와 ForeignKey 설정
    user = models.ForeignKey(User, on_delete=models.CASCADE) # User 와 ForeignKey 설정

    message = RichTextUploadingField('내용', max_length=3000) # 내용
    order = models.PositiveIntegerField('순서', default=0) # 내용

    created_at = models.DateTimeField('등록 날짜', auto_now_add=True, blank=True)  # 등록 날짜
    updated_at = models.DateTimeField('업데이트 날짜', auto_now=True, blank=True)  # 업데이트 날짜

    is_reply_to_reply = models.BooleanField('대댓글 여부', blank=True, default=False)
    reply_to_reply_address = models.PositiveIntegerField('대상댓글', blank=True, null=True)

    def __str__(self):
        return '{0}-ReplyChapter({1})'.format(self.video, self.pk)
##################################################################################################
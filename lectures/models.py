# from django.db import models
# from imagekit.models import ImageSpecField
# from imagekit.processors import Thumbnail
# from django.contrib.auth.models import User
# #from products.models import Product
# # Create your models here.
#
# class Section(models.Model):
#     title = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.title
#
#
# class Category(models.Model):
#     title = models.CharField( max_length=200)
#
#     def __str__(self):
#         return self.title
#
# class Lecture(models.Model):
#     section = models.ForeignKey(Section, on_delete=models.CASCADE)
#
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     material = models.ManyToManyField('products.Product')
#
#     title = models.CharField(max_length=200) #제목
#     added = models.DateTimeField(auto_now_add=True, blank=True) #등록한 날짜
#     updated = models.DateTimeField(auto_now=True, blank=True) #업데이트 날짜
#     description=models.CharField(max_length=500, blank=True) #간략한 설명
#     discount = models.IntegerField(default=0, blank=True) #할인 가격
#     isSale = models.BooleanField('For Sale', default=False) #판매 여부
#     lecture_image = models.ImageField(upload_to='lecture_image/', blank=True) #이미지
#     thumbnail = ImageSpecField(
#         source='lecture_image',
#         processors=[Thumbnail(600,400)],
#         format='JPEG',
#         options={'quality': 80})
#     sample = models.URLField(blank=True) #샘플영상
#     fee = models.IntegerField(default=0, blank=True) #가격
#
# ###############################추가 공통속성################################
#     isShow = models.BooleanField('On showing', default=False)
#     isDiscount = models.BooleanField('On Sale', default=False)
# #########################################################################
#
# #############################Lecture attribute###########################
#     content = models.TextField(blank=True, default='')
#     register_from = models.DateField(blank=True, null=True)
#     register_to = models.DateField(blank=True, null=True)
#     period_from = models.DateField(blank=True, null=True)
#     period_to = models.DateField(blank=True, null=True)
#     #book = models.CharField('교재 및 교보재', max_length=200, blank=True)
#     teacher = models.ManyToManyField(User)
#     location = models.CharField(max_length=300, blank=True)
# #########################################################################
#     def __str__(self):
#         return self.title
#
# class Video(models.Model):
#     lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     movie = models.URLField(blank=True)
#     content = models.TextField(max_length=3000, blank=True)
#     file = models.FileField(upload_to='data_file/lecture/', blank=True)
#
#

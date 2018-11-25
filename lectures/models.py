from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail
#from products.models import Product
# Create your models here.

class Section(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField( max_length=200)

    def __str__(self):
        return self.title

class Lecture(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    added = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    description=models.CharField(max_length=500, blank=True)
    content = models.TextField(blank=True, default='')
    lecture_image = models.ImageField(upload_to='lecture_image/', blank=True)
    thumbnail = ImageSpecField(
        source='lecture_image',
        processors=[Thumbnail(600,400)],
        format='JPEG',
        options={'quality': 80})
    register_from = models.DateField(blank=True, null=True)
    register_to = models.DateField(blank=True, null=True)
    period_from = models.DateField(blank=True, null=True)
    period_to = models.DateField(blank=True, null=True)
    fee = models.IntegerField(default=0, blank=True)
    discount = models.IntegerField(default=0, blank=True)
    isDiscount = models.BooleanField('On Sale', default=False)
    sample = models.URLField(blank=True)
    book = models.CharField('교재 및 교보재', max_length=200, blank=True)
    material = models.ManyToManyField('products.Product')
    teacher = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=300, blank=True)
    isSale = models.BooleanField('For Sale', default=False)
    isShow = models.BooleanField('On showing', default=False)

    def __str__(self):
        return self.title

class Video(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    movie = models.URLField(blank=True)
    content = models.TextField(max_length=3000, blank=True)
    file = models.FileField(upload_to='data_file/lecture/', blank=True)



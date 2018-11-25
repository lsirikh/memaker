from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

# Create your models here.




class Category(models.Model):
    title = models.CharField('Title', max_length=200, default='no title')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Product(models.Model):
    title = models.CharField('Title', max_length=200, default='no title')
    added = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    cost = models.IntegerField('Product price', default=0)
    discount = models.IntegerField('Discounted price', default=0)
    isSale = models.BooleanField('For Sale', default=False)
    description = models.CharField('Description', max_length=300)
    file = models.FileField(upload_to='data_file/product/', blank=True)
    product_image = models.ImageField(upload_to='product_image/', blank=True)
    thumbnail = ImageSpecField(
        source='product_image',
        processors=[Thumbnail(600,400)],
        format='JPEG',
        options={'quality' : 80})
    movie = models.URLField(blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    related_lec = models.ManyToManyField('lectures.Lecture')

    def __str__(self):
        return self.title


class Detail(models.Model):
    title = models.CharField(max_length=50, blank=True, default='')
    description = models.TextField('Content', max_length=3000, blank=True)
    image = models.ImageField(upload_to='product_image/', blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    upper_line = models.BooleanField('upper line', default=False)
    lower_line = models.BooleanField('lower line', default=False)

    def __str__(self):
        return str(self.pk)


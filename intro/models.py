from django.db import models
from django.urls import reverse

# Create your models here.
class Intro(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='content_image', blank=True)
    character = models.ImageField(upload_to='character_image', blank=True)
    content = models.TextField('CONTENT')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Intro, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('intro:index')

    class Meta:
        ordering = ['id']
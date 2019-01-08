from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

# Create your models here.

def user_directory_path(instance, filename):
    return "account_image/{id}_{user}/{file}".format(id=instance.user.id, user=instance.user, file=filename)


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('남', '남자'),
        ('여', '여자'),
    )
    REGISTER_ROUTE = (
        ('BLG', '네이버블로그'),
        ('SRC', '인터넷검색'),
        ('NWS', '뉴스 및 기사'),
        ('FBK', '페이스북'),
        ('ING', '인스타그램'),
        ('REC', '지인소개'),
        ('EDU', '강의교육'),
        ('ETC', '기타'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to= user_directory_path, blank=True, default='account_image/account_pic_default.png')
    thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(240, 240)],
        format='JPEG',
        options={'quality': 80})
    email_confirmed = models.BooleanField(default=False)
    description = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    route = models.CharField(max_length=5, choices=REGISTER_ROUTE, null=True, blank=True)
    agree = models.BooleanField(default=False)
    favorite = models.ManyToManyField('products.Content', blank=True)

    #favorite_product = models.ManyToManyField('products.Product', blank=True)
    #favorite_lecture = models.ManyToManyField('lectures.Lecture', blank=True)

    def __str__(self):
        return self.user.username



def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
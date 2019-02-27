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
    image = models.ImageField('사진', upload_to= user_directory_path, blank=True, default='account_image/account_pic_default.png')
    thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(240, 240)],
        format='JPEG',
        options={'quality': 80})
    email_confirmed = models.BooleanField('이메일검증', default=False)
    description = models.CharField('본인소개', max_length=200, blank=True, null=True)
    postal_code = models.CharField('우편번호', max_length=20, blank=True, null=True)
    address = models.CharField('주소', max_length=200, blank=True, null=True)
    extraAddress = models.CharField('참조주소', max_length=200, blank=True, null=True)
    detailAddress = models.CharField('상세주소', max_length=200, blank=True, null=True)
    phone = models.PositiveIntegerField('전화번호', blank=True, null=True)
    birth = models.DateField('생년월일', null=True, blank=True)
    gender = models.CharField('성별', max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    route = models.CharField('가입경로', max_length=5, choices=REGISTER_ROUTE, null=True, blank=True)
    agree = models.BooleanField('정보제공동의', default=False)
    favorite = models.ManyToManyField('products.Content', blank=True)

    #favorite_product = models.ManyToManyField('products.Product', blank=True)
    #favorite_lecture = models.ManyToManyField('lectures.Lecture', blank=True)

    def __str__(self):
        return self.user.username



def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
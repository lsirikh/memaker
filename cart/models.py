from django.db import models
from django.contrib.auth.models import User
from products.models import Content

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    cost = models.PositiveIntegerField('금액',default=0, null=True, blank=True)
    quantity = models.PositiveIntegerField('수량', default=1, null=True, blank=True)
    created_at = models.DateTimeField('생성일', auto_now_add=True)
    updated_at = models.DateTimeField('수정일', auto_now=True)


    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        ordering=('updated_at', 'created_at')

    def get_cost(self):
        return self.cost * self.quantity
from django.db import models
from products.models import Content
from accounts.models import UserProfile

# Create your models here.

class Order(models.Model):
    name = models.CharField('이름', max_length=50)
    phone = models.PositiveIntegerField('전화번호')
    address = models.CharField('주소', max_length=250)
    detailAddress = models.CharField('상세주소', max_length=250)
    extraAddress = models.CharField('참조주소', max_length=250)

    postal_code = models.CharField('우편번호', max_length=20)
    created = models.DateTimeField('주문요청', auto_now_add=True)
    updated = models.DateTimeField('주문수정', auto_now=True)
    totalCost = models.PositiveIntegerField('최종금액', default=0)
    paid = models.BooleanField('결제', default=False)
    infoSave = models.BooleanField('반영여부', default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE)
    content = models.ForeignKey(Content,
                                on_delete=models.CASCADE)
    cost = models.PositiveIntegerField('금액')
    quantity = models.PositiveIntegerField('수량', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.cost * self.quantity
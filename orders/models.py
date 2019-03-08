from django.db import models
from products.models import Content
from accounts.models import UserProfile

import datetime

# Create your models here.

# def generate_order_number():
#     try:
#         last_order = Order.objects.all().order_by('id').last()
#     except:
#         last_order = 0
#
#     dt = datetime.datetime.now()
#     gen_code = 'me' + str(dt.year) + str(dt.month) + \
#                str(dt.day) + str(dt.hour) + \
#                str(dt.minute) + str(dt.second)
#     if not last_order:
#         return gen_code + '0'
#     order_no = last_order.id + 1
#     new_order_no = gen_code + str(order_no)
#
#     return new_order_no

class Order(models.Model):
    order_no = models.CharField('주문번호', default=0, max_length=500, null=True, blank=True)
    name = models.CharField('이름', max_length=50)
    phone = models.CharField('전화번호', max_length=20, blank=True, null=True)
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
        return sum(item.get_cost() for item in self.orderitem.all())



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderitem',
                              on_delete=models.CASCADE)
    content = models.ForeignKey(Content,
                                on_delete=models.CASCADE)
    cost = models.PositiveIntegerField('금액')
    quantity = models.PositiveIntegerField('수량', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.cost * self.quantity
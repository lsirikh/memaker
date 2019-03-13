from django.db import models
from products.models import Content
from accounts.models import UserProfile
from django.contrib.auth.models import User

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
    DELIVERY_CATEGORY = (
        ('001', '상품준비중'),
        ('002', '배송준비중'),
        ('003', '배송중'),
        ('004', '배송완료'),
        ('005', '기타'),
    )

    DELIVERY_FEE = (
        ('001', '일반배송'),
        ('002', '도서산간'),
        ('003', '착불'),
        ('004', '직접수령'),
        ('005', '기타'),
    )

    CONFIRM_CAT = (
        ('001', '미정'),
        ('002', '확정'),
    )

    PAYMENT_OF_METHOD = (
        ('card', '신용카드'),
        ('trans', '실시간계좌이체'),
        ('vbank', '가상계좌'),
        ('phone', '휴대폰소액결제'),
        ('samsung', '삼성페이 '),
        ('kpay', 'KPay'),
        ('cultureland', '문화상품권 '),
        ('smartculture', '스마트문상 '),
        ('happymoney', '해피머니 '),
    )

    PAYMENT_STATUS = (
        ('ready', '미결제'),
        ('paid', '결제완료'),
        ('cancelled', '결제취소'),
        ('failed', '결제실패'),
    )

    user = models.ForeignKey(User, related_name='order', default='', on_delete=models.CASCADE)
    order_no = models.CharField('주문번호', default=0, max_length=500, null=True, blank=True)
    imp_uid = models.CharField('아임포트', default=0, max_length=500, null=True, blank=True)
    name = models.CharField('이름', max_length=50)
    phone = models.CharField('전화번호', max_length=20, blank=True, null=True)
    address = models.CharField('주소', max_length=250)
    detailAddress = models.CharField('상세주소', max_length=250)
    extraAddress = models.CharField('참조주소', max_length=250)

    postal_code = models.CharField('우편번호', max_length=20)
    created = models.DateTimeField('주문요청', auto_now_add=True)
    updated = models.DateTimeField('주문수정', auto_now=True)
    totalCost = models.PositiveIntegerField('최종금액', default=0)
    method = models.CharField('결제수단', max_length=10, choices=PAYMENT_OF_METHOD, default='card')
    paid = models.CharField('결제상태', max_length=10, choices=PAYMENT_STATUS, default='ready')
    delivery_fee = models.CharField('배송료', max_length=4, choices=DELIVERY_FEE, default='001')
    delivery = models.CharField('배송상태', max_length=4, choices=DELIVERY_CATEGORY, default='001')
    confirm = models.CharField('구매결정', max_length=4, choices=CONFIRM_CAT, default='001')
    note = models.CharField('요청사항', max_length=250, default='', blank=True, null=True)
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
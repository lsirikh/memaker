from django.db import models
from products.models import Content
from accounts.models import UserProfile
from django.contrib.auth.models import User

import datetime


class Order(models.Model):

    CONFIRM_CAT = (
        ('001', '미정'),
        ('002', '확정'),
        ('003', '취소'),
    )

    user = models.ForeignKey(User, related_name='order', default='', on_delete=models.CASCADE)

    merchant_uid = models.CharField('주문번호', default=0, max_length=500, null=True, blank=True)
    imp_uid = models.CharField('아임포트', default=0, max_length=500, null=True, blank=True)

    created = models.DateTimeField('주문일자', auto_now_add=True)
    updated = models.DateTimeField('주문수정', auto_now=True)

    totalCost = models.PositiveIntegerField('최종금액', default=0)
    tex_free_cost = models.PositiveIntegerField('면세금액', default=0, null=True, blank=True)

    confirm = models.CharField('구매결정', max_length=4, choices=CONFIRM_CAT, default='001')
    isDirect= models.BooleanField('바로구매', default=False, null=True, blank=True)
    result= models.BooleanField('구매상태', default=False, null=True, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.orderitem.all())


class ImportInfo(models.Model):
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

    order = models.OneToOneField(Order, related_name='importInfo',
                                 on_delete=models.CASCADE)
    amount = models.CharField(default=None, max_length=500, null=True, blank=True)
    apply_num = models.CharField(default=None, max_length=500, null=True, blank=True)
    bank_code = models.CharField(default=None, max_length=500, null=True, blank=True)
    bank_name = models.CharField(default=None, max_length=500, null=True, blank=True)
    buyer_addr = models.CharField(default=None, max_length=500, null=True, blank=True)
    buyer_email = models.CharField(default=None, max_length=500, null=True, blank=True)
    buyer_name = models.CharField(default=None, max_length=500, null=True, blank=True)
    buyer_postcode = models.CharField(default=0, max_length=500, null=True, blank=True)
    buyer_tel = models.CharField(default=0, max_length=500, null=True, blank=True)
    cancel_amount = models.CharField(default=0, max_length=500, null=True, blank=True)
    cancel_history = models.CharField(default=None, max_length=500, null=True, blank=True)
    cancel_reason = models.CharField(default=None, max_length=500, null=True, blank=True)
    cancel_receipt_urls = models.CharField(default=None, max_length=500, null=True, blank=True)
    cancelled_at = models.CharField(default=None, max_length=500, null=True, blank=True)
    card_code = models.CharField(default=None, max_length=500, null=True, blank=True)
    card_name = models.CharField(default=None, max_length=500, null=True, blank=True)
    card_quota = models.CharField(default=0, max_length=500, null=True, blank=True)
    cash_receipt_issued = models.CharField(default=None, max_length=500, null=True, blank=True)
    channel = models.CharField(default=None, max_length=500, null=True, blank=True)
    currency = models.CharField(default='KRW', max_length=500, null=True, blank=True)
    custom_data = models.CharField(default=None, max_length=500, null=True, blank=True)
    escrow = models.CharField(default=None, max_length=500, null=True, blank=True)
    fail_reason = models.CharField(default=None, max_length=500, null=True, blank=True)
    failed_at = models.CharField(default=None, max_length=500, null=True, blank=True)
    imp_uid = models.CharField(default=None, max_length=500, null=True, blank=True)
    merchant_uid = models.CharField(default=None, max_length=500, null=True, blank=True)
    name = models.CharField(default=None, max_length=500, null=True, blank=True)
    paid_at = models.CharField(default=0, max_length=500, null=True, blank=True)
    pay_method = models.CharField(default=None, choices=PAYMENT_OF_METHOD, max_length=500, null=True, blank=True)
    pg_id = models.CharField(default=None, max_length=500, null=True, blank=True)
    pg_provider = models.CharField(default=None, max_length=500, null=True, blank=True)
    pg_tid = models.CharField(default=None, max_length=500, null=True, blank=True)
    receipt_url = models.CharField(default=None, max_length=500, null=True, blank=True)
    status = models.CharField(default=None, choices=PAYMENT_STATUS, max_length=500, null=True, blank=True)
    user_agent = models.CharField(default='sorry_not_supported_anymore', max_length=500, null=True, blank=True)
    vbank_code = models.CharField(default=None, max_length=500, null=True, blank=True)
    vbank_date = models.CharField(default=0, max_length=500, null=True, blank=True)
    vbank_holder = models.CharField(default=None, max_length=500, null=True, blank=True)
    vbank_issued_at = models.CharField(default=0, max_length=500, null=True, blank=True)
    vbank_name = models.CharField(default=None, max_length=500, null=True, blank=True)
    vbank_num = models.CharField(default=None, max_length=500, null=True, blank=True)

    def __str__(self):
        return 'ImportInfo {}'.format(self.merchant_uid)

class OrderDelivery(models.Model):
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

    DELIVERY_AGENT = (
        ('04', 'CJ대한통운'),
        ('05', '한진택배'),
        ('08', '롯데택배'),
        ('01', '우체국택배'),
        ('06', '로젠택배'),
        ('07', 'KG로지스택배'),
        ('09', 'KG로지스택배(KG옐로우캡)'),
        ('10', 'KGB택배'),
        ('11', '일양로지스'),
        ('12', 'EMS'),
        ('13', 'DHL'),
        ('20', '한덱스'),
        ('21', 'FedEx'),
        ('14', 'UPS'),
        ('26', 'USPS'),
        ('22', '대신택배'),
        ('23', '경동택배'),
        ('32', '합동택배'),
        ('46', 'CU 편의점택배'),
        ('24', 'CVSnet 편의점택배'),
        ('25', 'TNT Express'),
        ('16', '한의사랑택배'),
        ('15', 'GTX로지스'),
        ('17', '천일택배'),
        ('18', '건영택배'),
        ('28', 'GSMNtoN'),
    )

    order = models.OneToOneField(Order, related_name='orderDelivery',
                                 on_delete=models.CASCADE)
    delivery_fee = models.CharField('배송료', max_length=4, choices=DELIVERY_FEE, default='001')
    delivery_status = models.CharField('배송상태', max_length=4, choices=DELIVERY_CATEGORY, default='001')
    delivery_agent = models.CharField('배송업체', default=None, choices=DELIVERY_AGENT, max_length=3, null=True, blank=True)
    delivery_code = models.CharField('운송장', default=None, max_length=500, null=True, blank=True)

    delivery_note = models.CharField('배송사항', default=None, max_length=500, null=True, blank=True)

    name = models.CharField('이름', max_length=50, blank=True, null=True)
    email = models.EmailField('이메일', max_length=20, blank=True, null=True)
    phone = models.CharField('전화번호', max_length=20, blank=True, null=True)
    address = models.CharField('주소', max_length=250, blank=True, null=True)
    detailAddress = models.CharField('상세주소', max_length=250, blank=True, null=True)
    extraAddress = models.CharField('참조주소', max_length=250, blank=True, null=True)
    postal_code = models.CharField('우편번호', max_length=20, blank=True, null=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderItem',
                              on_delete=models.CASCADE)
    content = models.ForeignKey(Content,
                                on_delete=models.CASCADE)
    cost = models.PositiveIntegerField('금액')
    quantity = models.PositiveIntegerField('수량', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.cost * self.quantity

class OrderCancel(models.Model):
    order = models.OneToOneField(Order, related_name='orderCancel',
                              on_delete=models.CASCADE)
    merchant_uid = models.CharField('주문번호', max_length=100, default='', blank=True, null=True)
    note = models.CharField('사유', max_length=250, default='', blank=True, null=True)
    created = models.DateTimeField('취소일자', auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        ordering = ('-created',)
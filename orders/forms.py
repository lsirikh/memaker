from django import forms
from orders.models import Order
from django.core.validators import RegexValidator, DecimalValidator

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
                'method',
                'delivery_fee',  # 배송비 정보
                'note',  # 배송시 유의사항
                'name',
                'phone',
                'email',
                'postal_code',
                'address', #자동완성 주소
                'extraAddress', #자동완성 참조주소
                'detailAddress',  # 세부 주소내용
                'infoSave'
                  ]

    DELIVERY_FEE = (
        ('001', '일반배송(2,500원)'),
        ('002', '도서산간(5,000원)'),
        ('003', '착불'),
        ('004', '직접수령'),
        ('005', '기타'),
    )

    PAYMENT_OF_METHOD = (
        ('card', '신용카드'),
        ('trans', '실시간계좌이체'),
        ('vbank', '가상계좌'),
        # ('phone', '휴대폰소액결제'),
        # ('samsung', '삼성페이 '),
        # ('kpay', 'KPay'),
        # ('cultureland', '문화상품권 '),
        # ('smartculture', '스마트문상 '),
        # ('happymoney', '해피머니 '),
    )



    numeric = RegexValidator(r'^[0-9]*$', '숫자만 허용됩니다.')

    # def clean(self):
    #     cleaned_data = super(OrderCreateForm, self).clean()
    #
    # def clean_phone(self):
    #     phone = self.cleaned_data['phone']
    #     print(phone)
    #     try:
    #         DecimalValidator(phone)
    #         print("숫자로 된 전화번호가 맞습니다.")
    #     except:
    #         print("숫자로 된 전화번호가 아닙니다.")
    #         raise forms.ValidationError("전화번호가 올바르지 않습니다.")

    # imp_uid = forms.CharField(required=False,
    #                           initial=False,
    #                           widget=forms.HiddenInput(attrs={
    #                               'id': 'imp_uid'
    #                           }))

    method = forms.ChoiceField(
        label='결제수단',
        required=True,
        initial='card',
        help_text="결제하실 수단을 선택해주세요.",
        choices = PAYMENT_OF_METHOD,
        widget=forms.Select(
            attrs={
            'id': 'method',
            'class': 'form-control'}))

    delivery_fee = forms.ChoiceField(
        label='배송료',
        required=True,
        initial='001',
        help_text="해당 지역에 맞게 배송비 입력 바랍니다.예) 제주도:도서산간 등",
        choices = DELIVERY_FEE,
        widget=forms.Select(
            attrs={
            'id': 'delivery_fee',
            'class': 'form-control'}))

    note = forms.CharField(
        label='요청사항',
        required=False,
        max_length=50,
        help_text="배송시 요청사항을 남겨주세요.(최대 50자)",
        widget=forms.Textarea(attrs={
            'rows': 2,
            'id': 'note',
            'class': 'form-control'}))

    name = forms.CharField(
        label='이름',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': True}))

    email = forms.CharField(
        label='이메일',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': True}))

    phone = forms.CharField(
        validators=[numeric],
        label='휴대전화',
        required=True,
        max_length=11,
        help_text='01012345678 \'-\'를 제외한 숫자를 입력해주세요.',
        widget=forms.TextInput(attrs={
            'class': 'form-control'}))

    postal_code = forms.IntegerField(
        label='우편번호',
        required=True,
        help_text='우편번호를 입력하세요.',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'postcode',
            'placeholder': '우편번호',
            'readonly': True}))

    address = forms.CharField(
        label='주소',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id':'address',
            'readonly':True}))

    extraAddress = forms.CharField(
        label='참조주소',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'extraAddress',
            'readonly':True}))

    detailAddress = forms.CharField(
        label='상세주소',
        required=True,
        help_text='나머지 주소를 입력해주세요.',

        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id':'detailAddress'}))

    infoSave = forms.BooleanField(
        label='회원정보 반영',
        required=False,
        help_text="반영된 정보로 이후 결제에 활용됩니다.",
        widget=forms.CheckboxInput()
    )

class NewOrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
                    'order_no',
                    'name',
                  'phone',
                  'postal_code',
                  'address', #자동완성 주소
                  'extraAddress', #자동완성 참조주소
                  'detailAddress', #세부 주소내용
                  'infoSave'
                  ]

    order_no = forms.CharField(required=True,
                                widget=forms.HiddenInput)

    name = forms.CharField(
        label='이름',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    phone = forms.IntegerField(
        max_value=9999999999,
        label='휴대전화',
        required=True,
        help_text='01012345678 \'-\'를 제외한 숫자를 입력해주세요.',
        widget=forms.NumberInput(attrs={
            'class': 'form-control'}))

    postal_code = forms.IntegerField(
        label='우편번호',
        required=True,
        help_text='우편번호를 입력하세요.',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'postcode',
            'placeholder': '우편번호',
            'readonly': True}))

    address = forms.CharField(
        label='주소',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id':'address',
            'readonly':True}))

    extraAddress = forms.CharField(
        label='참조주소',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'extraAddress',
            'readonly':True}))

    detailAddress = forms.CharField(
        label='상세주소',
        required=True,
        help_text='나머지 주소를 입력해주세요.',

        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id':'detailAddress'}))

    infoSave = forms.BooleanField(
        label='회원정보 반영',
        required=False,
        help_text="반영된 정보로 이후 결제에 활용됩니다.",
        widget=forms.CheckboxInput()
    )
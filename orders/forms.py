from django import forms
from orders.models import Order
from django.core.validators import RegexValidator, DecimalValidator

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name',
                  'phone',
                  'postal_code',
                  'address', #자동완성 주소
                  'extraAddress', #자동완성 참조주소
                  'detailAddress', #세부 주소내용
                  'infoSave'
                  ]

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

    name = forms.CharField(
        label='이름',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': True}))

    phone = forms.CharField(
        validators=[numeric],
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
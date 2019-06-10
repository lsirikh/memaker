from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    PasswordChangeForm,
    UserCreationForm,
    UserChangeForm)

from accounts.models import UserProfile
from django.core.validators import RegexValidator


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class FindIdForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='기존 비밀번호',
        help_text='기존의 비밀번호를 입력해주세요.',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(
        label='신규 비밀번호',
        help_text='변경할 비밀번호를 입력해주세요.',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(
        label='기존 비밀번호 확인',
        help_text='비밀번호를 다시 한 번 입력해주세요.',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class WithdrawalForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('password', )

    password = forms.CharField(
        label='기존 비밀번호',
        help_text='기존의 비밀번호를 입력해주세요.',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegistrationForm(UserCreationForm):


    username = forms.CharField(max_length=30,
                               label='아이디',
                               widget=forms.TextInput(
                                   attrs={
                                       'size':20,
                                       'class': 'form-control',
                                       'title': '아이디를 입력하세요.',
                                   }))
    first_name = forms.CharField(max_length=30,
                                 label='이름',
                                 widget=forms.TextInput(attrs={
                                     'size':20,
                                     'class': 'form-control',
                                     'title': '이름 또는 별명을 입력하세요.',
                                 }),
                                 help_text='실명을 입력해 주세요.')
    email = forms.EmailField(max_length=254,
                             label='이메일',
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'title': '이메일은 검증을 위해 반드시 필요합니다.',
                             }),
                             required=True,
                             help_text='사용 가능한 이메일을 입력해 주세요.')

    password1 = forms.CharField(label='비밀번호',
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                }),
                                help_text='*비밀번호는 아이디 혹은 개인 정보와 유사하게 만들 수 없습니다.\n' \
                                          '*비밀번호는 최소 8자리 이상으로 구성하셔야 합니다.\n' \
                                          '*비밀번호는 간단한 규칙이나 일반적인 단어를 사용하 만들 수 없습니다.\n' \
                                          '*비밀번호는 숫자와 문자를 조합하여 만들어야 합니다.')
    password2 = forms.CharField(label='비밀번호 확인',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text='비밀번호를 다시 한 번 입력해주세요.')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user



class RegistrationProfileForm(UserChangeForm):
    def __init__(self, *args, **kargs):
        super(UserChangeForm, self).__init__(*args, **kargs)
        del self.fields['password']

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

    route = forms.ChoiceField(
        label='가입경로',
        required=False,
        help_text="회원 가입시 \'미메이커\'사이트를 알게 되신 경로를 말씀해 주세요.",
        widget=forms.RadioSelect(),
        choices=REGISTER_ROUTE)

    agree = forms.BooleanField(
        label = '개인 정보 제공 동의 및 서비스 이용 약관 동의',
        required=True,
        help_text= "회원 가입에 관한 정보를 제공합니다.",
        widget=forms.CheckboxInput(attrs={'class': 'form-inline'})
    )

    class Meta:
        model = UserProfile
        fields = (
            'route',
            'agree',
        )

    def save(self, commit=True):
        userprofile = super(RegistrationProfileForm, self).save(commit=False)
        userprofile.route = self.cleaned_data['route']
        userprofile.agree = self.cleaned_data['agree']

        if commit:
            userprofile.save()

        return userprofile




#class UserEditForm(forms.ModelForm):
class UserEditForm(UserChangeForm):
    def __init__(self, *args, **kargs):
        super(UserChangeForm, self).__init__(*args, **kargs)
        del self.fields['password']

    class Meta:
        model = User
        #fields = ('first_name', 'email')
        fields = ('first_name',)


    first_name = forms.CharField(
        label='이  름',
        required=True,
        help_text='이름 또는 닉네임을 적어주세요.',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        )
    #email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))


#class ProfileEditForm(forms.ModelForm):
class ProfileEditForm(UserChangeForm):
    def __init__(self, *args, **kargs):
        super(UserChangeForm, self).__init__(*args, **kargs)
        del self.fields['password']

    class Meta:
        model = UserProfile
        fields = ('image',
                  'gender',
                  'birth',
                  'postal_code',
                  'address',
                  'extraAddress',
                  'detailAddress',
                  'phone',
                  'description',
                  'route',
                  )

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

    image = forms.ImageField(
        label='사  진',
        required=False,
        help_text='정사각형 형태의 이미지 파일을 등록해 주세요. 예) 가로 400px 세로 400px',
        widget=forms.FileInput(attrs={'class': 'form-control'})
        )
    gender = forms.ChoiceField(
        label='성  별',
        required=False,
        help_text='성별을 선택해주세요.',
        widget=forms.RadioSelect(), choices=GENDER_CHOICES)
    route = forms.ChoiceField(
        label='가입경로',
        required=False,
        help_text="회원 가입시 \'미메이커\'사이트를 알게 되신 경로를 말씀해 주세요.",
        widget=forms.RadioSelect(), choices=REGISTER_ROUTE)
    birth = forms.DateField(
        label='생년월일',
        required=False,
        help_text='ex)1994-02-22',
        widget=forms.DateInput(attrs={'class': 'form-control'}))

    numeric = RegexValidator(r'^[0-9]*$', '숫자만 허용됩니다.')

    phone = forms.CharField(
        validators=[numeric],
        label='휴대전화',
        required=False,
        help_text='01012345678 \'-\'를 제외한 숫자를 입력해주세요.',
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    postal_code = forms.CharField(
        label='우편번호',
        required=False,
        help_text='배송이나 우편물 전달을 위해 정확한 주소를 기입해주세요.',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'postcode',
            'placeholder': '우편번호',
            'readonly': True
        }))
    address = forms.CharField(
        label='주  소',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id':'address',
            'readonly':True
        }))
    extraAddress = forms.CharField(
        label='참조주소',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'extraAddress',
            'readonly':True}))
    detailAddress = forms.CharField(
        label='상세주소',
        required=False,
        help_text='배송이나 우편물 전달을 위해 정확한 주소를 기입해주세요.',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'detailAddress',
        }))
    description = forms.CharField(
        label='자기소개',
        required=False,
        help_text='자신에 관한 간단한 소개를 남겨주세요.',
        widget=forms.Textarea(attrs={'class': 'form-control'}))

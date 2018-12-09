from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    PasswordChangeForm,
    UserCreationForm,
    UserChangeForm)

from accounts.models import UserProfile


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
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30,
                                 label='이름',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=254,
                             label='이메일',
                             widget=forms.EmailInput(attrs={'class': 'form-control'}),
                             required=True,
                             help_text='사용 가능한 이메일을 입력해 주세요.')

    password1 = forms.CharField(label='비밀번호',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
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
        fields = ('gender',
                  'birth',
                  'address',
                  'phone',
                  'description')

    GENDER_CHOICES = (
        ('남', '남자'),
        ('여', '여자'),
    )

    gender = forms.ChoiceField(
        label='성  별',
        required=False,
        help_text='성별을 선택해주세요.',
        widget=forms.RadioSelect(), choices=GENDER_CHOICES)
    birth = forms.DateField(
        label='생년월일',
        required=False,
        help_text='ex)1994-02-22',
        widget=forms.DateInput(attrs={'class': 'form-control'}))
    phone = forms.IntegerField(
        max_value=9999999999,
        label='휴대전화',
        required=False,
        help_text='01012345678 \'-\'를 제외한 숫자를 입력해주세요.',
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    address = forms.CharField(
        label='주  소',
        required=False,
        help_text='배송이나 우편물 전달을 위해 정확한 주소를 기입해주세요.',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(
        label='자기소개',
        required=False,
        help_text='자신에 관한 간단한 소개를 남겨주세요.',
        widget=forms.Textarea(attrs={'class': 'form-control'}))

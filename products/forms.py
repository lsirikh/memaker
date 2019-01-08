from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    PasswordChangeForm,
    UserCreationForm,
    UserChangeForm)

from products.models import(
    Appraisal,
    ReplyChapter
)
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AppraisalForm(forms.ModelForm):
    class Meta:
        model = Appraisal
        fields = ['rate', 'message' ]

    RATE = (
        (5, '★★★★★'),
        (4, '★★★★☆'),
        (3, '★★★☆☆'),
        (2, '★★☆☆☆'),
        (1, '★☆☆☆☆'),

    )

    rate = forms.ChoiceField(
        label='리뷰점수',
        required=True,
        help_text="평가 점수를 알려주세요.",
        widget=forms.Select,
        choices=RATE)

    message = forms.CharField(
        label='리뷰내용',
        required=True,
        help_text='리뷰의견을 간단하게 적어주세요. 500자 이내',
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

class ReplyChapterForm(forms.ModelForm):
    class Meta:
        model = ReplyChapter
        fields = ['message',]

    message = forms.CharField(
        label='내용',
        required=True,
        #id='ckeditor',
        widget=CKEditorUploadingWidget(
            attrs={'autofocus':True}
        ),
        help_text="2000자 이내로 작성해주세요..."
    )
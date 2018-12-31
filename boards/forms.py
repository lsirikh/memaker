from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    PasswordChangeForm,
    UserCreationForm,
    UserChangeForm)

from boards.models import Board, Post, Topic

from ckeditor_uploader.widgets import CKEditorUploadingWidget

class NewContentForm(forms.ModelForm):


    title = forms.CharField(max_length=255,
                               label='제목',
                               required=True,
                               widget=forms.TextInput(attrs={'autofocus':'autofocus',
                                                             'class': 'form-control'}))
    message = forms.CharField(
        label='내용',
        required=True,
        #id='ckeditor',
        widget=CKEditorUploadingWidget(attrs={'autofocus':True}),
        max_length=4000,
        help_text="4000자 이내로 작성해주세요...",
    )



    class Meta:
        model = Topic
        fields = ['title', 'message',]

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message',]

    message = forms.CharField(
        label='내용',
        required=True,
        #id='ckeditor',
        widget=CKEditorUploadingWidget(
            attrs={'autofocus':True}
        ),
        help_text="4000자 이내로 작성해주세요..."
    )
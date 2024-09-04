from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    nickname = forms.CharField(label="닉네임")

    class Meta:
        model = CustomUser
        fields = ("username", "password1", "password2", "nickname", "email")
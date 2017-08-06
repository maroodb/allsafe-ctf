from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from blog.models import News
from members.models import Member


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class ArticleForm(forms.Form):
    image = forms.ImageField(label="image")


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'last_name', 'first_name',)


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('avatar', 'status',)


class ImageForm(forms.Form):
    image = forms.ImageField()


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ('publisher', 'date')


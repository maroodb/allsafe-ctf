from django import forms


class ConnexionForm(forms.Form):

    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class ArticleForm (forms.Form):
    image = forms.ImageField(label="image")





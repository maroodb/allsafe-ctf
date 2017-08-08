from django import forms

from magazine.models import NewsLettre


class NewsLettreForm(forms.ModelForm):
    class Meta:
        model = NewsLettre
        fields = '__all__'

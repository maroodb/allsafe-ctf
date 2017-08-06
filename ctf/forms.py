from django import forms

from ctf.models import Challenge


class UploadForm(forms.ModelForm):
    class Meta:
        model = Challenge
        exclude = ('uploader', 'resolvers', 'date')



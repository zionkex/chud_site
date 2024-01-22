from django import forms
from .models import PhotoPost, Fileupload


class PhotoPostForm(forms.ModelForm):
    class Meta:
        model = PhotoPost
        fields = ['title', 'body', 'images']
        widgets = {
            'images': forms.CheckboxSelectMultiple(),
        }


class FileuploadForm(forms.ModelForm):
    class Meta:
        model = Fileupload
        fields = ['title', 'file']

from django import forms
from .models import PhotoPost

class PhotoPostForm(forms.ModelForm):
    class Meta:
        model = PhotoPost
        fields = ['title', 'body', 'images']
        widgets = {
            'images': forms.CheckboxSelectMultiple(),
        }

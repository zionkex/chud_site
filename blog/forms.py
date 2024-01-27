from django import forms
from .models import Fileupload, Post


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)
    author = forms.CharField(max_length=50)
    main_image = forms.ImageField(required=False)
    images = MultipleFileField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        main_image = cleaned_data.get('main_image')
        images = cleaned_data.get('images')

        return cleaned_data

class FileuploadForm(forms.ModelForm):
    class Meta:
        model = Fileupload
        fields = ['title', 'file']

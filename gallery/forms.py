from django import forms
from .models import ImageUnit

class ImageFieldForm(forms.ModelForm):
    # image_field = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': False}))

    class Meta:
        model = ImageUnit
        fields = [
            'image_title',
            'image_category',
            'image_field',
        ]


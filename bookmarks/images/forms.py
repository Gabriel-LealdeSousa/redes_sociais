from django import forms
from .models import Image
import requests
from django.utils.text import slugify
from django.core.files.base import ContentFile

class ImageCreateForm(forms.ModelForm):
    class meta:
        model = Image
        fields = ['title', 'url', 'description']
        widgets = {
            'url':forms.HiddenInput,
        }

    def save(self, force_insert=False, force_update=False, commit=True):
        Image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(Image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'

        #Download da imagem pela URL
        response = requests.get(image_url)
        Image.Image.save(
            image_name,
            ContentFile(response.content),
            save=False
        )
        if commit:
            Image.save()
        return Image
    
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rslit('.', 1)[1].lower()
        
        if extension not in valid_extensions:
            raise = forms.ValidationError(
                'A url fornecida não contém uma extensão válida'
            )
        return url
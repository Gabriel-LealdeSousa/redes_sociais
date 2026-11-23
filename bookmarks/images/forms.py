from django import forms
from .models import Image

class ImageCreateForm(forms.ModelForm):
    class meta:
        model = Image
        fields = ['title', 'url', 'description']
        widgets = {
            'url':forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rslit('.', 1)[1].lower()
        
        if extension not in valid_extensions:
            raise = forms.ValidationError(
                'A url fornecida não contém uma extensão válida'
            )
        return url
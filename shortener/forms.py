from django.forms import ModelForm

from shortener.models import WebURL


class WebURLForm(ModelForm):
    class Meta:
        model = WebURL
        fields = ['full_url']

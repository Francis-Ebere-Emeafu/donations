from django import forms
from tinymce.widgets import TinyMCE

from news.models import NewsPost


class NewsForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 120, 'rows': 20}))

    class Meta:
        model = NewsPost
        exclude = []

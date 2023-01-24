from django import forms
from .models import Pictures

class SearchForm(forms.Form):
    keyword = forms.CharField(label = '検索', max_length=100)

class PictureForm(forms.ModelForm):
    class Meta:
        model = Pictures
        fields = ('content', 'user_name')
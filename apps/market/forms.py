from typing import Any
from django import forms
from apps.market.models import Product, Categoriy
from apps.users.models import AuthorCardMarket


class CreateProductForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={
        "type":"file", "id":"form-submit", "class":"orange-button"
    }))
    title = forms.CharField(widget=forms.TextInput(attrs={
        "type":"title","name":"title", "id":"title", "placeholder":"Ex. Lyon King", "autocomplete":"on"
    }))
    desciptions = forms.CharField(widget=forms.TextInput(attrs={
        "type":"description", "name":"description", "id":"description","placeholder":"Give us your idea", "autocomplete":"on"
    }))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={
        "type":"price", "name":"price", "id":"price", "placeholder":"rice depends on quality. Ex. 0.06 ETH", "autocomplete":"on"
    }))
  
    class Meta:
        model = Product
        fields = ['image', 'title', 'desciptions', 'price', 'categories', 'count', 'ovner']
    
class CardForm(forms.ModelForm):
    class Meta:
        model = AuthorCardMarket
        fields = ['proruct_count']
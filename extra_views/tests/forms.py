from django import forms
from models import Order, Item


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        

class AddressForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    line1 = forms.CharField(max_length=255, required=False)
    line2 = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=255, required=False)
    postcode = forms.CharField(max_length=10, required=True)

from django import forms
from .models import Product
from dal import autocomplete


class QueryForm(forms.ModelForm):
    product_query = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        widget=autocomplete.ModelSelect2(url='product-autocomplete')
    )

    class Meta:
        model = Product
        fields = '__all__'

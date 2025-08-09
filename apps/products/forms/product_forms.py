from django import forms
from apps.products.models.product import Product
from apps.categories.models.category import Category

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        label='Category',
        queryset=Category.objects.all(),
        empty_label='Select Category',
        widget=forms.Select(attrs={
            'style': 'width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;'
        })
    )

    name = forms.CharField(
        label='Product Name',
        widget=forms.TextInput(attrs={
            'style': 'width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;',
            'placeholder': 'Enter product name'
        })
    )

    description = forms.CharField(
        label='Description',
        required=False,
        widget=forms.Textarea(attrs={
            'style': 'width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;',
            'placeholder': 'Product description',
            'rows': 4
        })
    )
    
    price = forms.DecimalField(
        label='Price',
        widget=forms.NumberInput(attrs={
            'style': 'width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;',
            'placeholder': '0.00',
            'step': '0.01',
            'min': '0'
        })
    )
    
    stock = forms.IntegerField(
        label='Stock',
        widget=forms.NumberInput(attrs={
            'style': 'width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;',
            'placeholder': '0',
            'min': '0'
        })
    )

    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'stock']

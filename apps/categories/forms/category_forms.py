from django import forms
from apps.categories.models.category import Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        label='Category Name',
        widget=forms.TextInput(attrs={
            'style': 'width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;',
            'placeholder': 'Enter category name'
        })
    )
    
    description = forms.CharField(
        label='Description',
        required=False,
        widget=forms.Textarea(attrs={
            'style': 'width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;',
            'placeholder': 'Enter category description',
            'rows': 4
        })
    )

    class Meta:
        model = Category
        fields = ['name', 'description']

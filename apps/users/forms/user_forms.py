# StockManagement/forms.py (veya accounts/forms.py — nerede tutuyorsanız)

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES,
        widget=forms.Select(attrs={
            'style': 'width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;'
        }),
        label='User Role',
        help_text='Admin: Full permissions, Manager: Product and category management, User: View only'
    )
    
    first_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'style': 'width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;'}),
        label='First Name'
    )
    
    last_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'style': 'width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;'}),
        label='Last Name'
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'style': 'width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;'}),
        label='Email Address'
    )
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={'style': 'width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;'}),
        label='Username'
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'style': 'width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;'}),
        label='Password'
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'style': 'width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;'}),
        label='Confirm Password'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'password1', 'password2']


class CustomUserChangeForm(UserChangeForm):
    password = None  # don't show password
    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES,
        widget=forms.Select(attrs={
            'style': 'width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;'
        }),
        label='User Role',
        help_text='Admin: Full permissions, Manager: Product and category management, User: View only'
    )
    
    first_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'style': 'width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;'}),
        label='First Name'
    )
    
    last_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'style': 'width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;'}),
        label='Last Name'
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'style': 'width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;'}),
        label='Email Address'
    )
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={'style': 'width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;'}),
        label='Username'
    )
    
    is_active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'style': 'margin-right: 0.5rem;'}),
        label='Active User',
        help_text='User must be active to access the system'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'is_active']

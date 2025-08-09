#!/usr/bin/env python
"""
Script to add default categories to the database
"""
import os
import django

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProductManagement.settings')
django.setup()

from StockManagement.models.category import Category

def add_default_categories():
    """Add default categories to the database"""
    
    categories = [
        {
            'name': 'Technology / Electronics',
            'description': 'Electronic devices, computer parts, and technology products'
        },
        {
            'name': 'Home & Living',
            'description': 'Home decoration, kitchenware, and lifestyle products'
        },
        {
            'name': 'Personal Care & Cosmetics',
            'description': 'Cosmetics, personal care, and beauty products'
        },
        {
            'name': 'Pet Products',
            'description': 'Food, toys, and care products for pets'
        }
    ]
    
    print("Adding categories...")
    
    for cat_data in categories:
        # Check if the category already exists
        if not Category.objects.filter(name=cat_data['name']).exists():
            category = Category.objects.create(**cat_data)
            print(f"✅ Category added: {category.name}")
        else:
            print(f"⚠️  Category already exists: {cat_data['name']}")
    
    print("\n🎉 Categories added successfully!")
    print(f"Total number of categories: {Category.objects.count()}")

if __name__ == '__main__':
    add_default_categories()

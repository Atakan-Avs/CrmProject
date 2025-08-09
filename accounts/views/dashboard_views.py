from django.shortcuts import render
from django.db.models import Count
from apps.products.models.product import Product
from apps.categories.models.category import Category

def dashboard_view(request):
    # Toplam ürün sayısı
    total_products = Product.objects.count()

    # Toplam kategori sayısı
    total_categories = Category.objects.count()

    # "Aktif" kabul edilecek, en az bir ürünü olan kategori sayısı
    active_categories = Category.objects \
        .annotate(num_products=Count('products')) \
        .filter(num_products__gt=0) \
        .count()

    # Ortalama ürün/adet (kategori başına)
    avg_per_category = total_products / total_categories if total_categories else 0

    context = {
        'total_products_count': total_products,
        'categories_count': total_categories,
        'active_categories_count': active_categories,
        'avg_products_per_category': round(avg_per_category, 2),
    }
    return render(request, 'dashboard.html', context)

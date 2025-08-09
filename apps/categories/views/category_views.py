from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.categories.models.category import Category
from apps.products.models.product import Product
from django.core.paginator import Paginator 
from apps.categories.forms.category_forms import CategoryForm
from django.db.models import Count, Q, F, ExpressionWrapper, FloatField

@login_required
def category_list(request):
    # 1) Başlangıç queryset'i: her kategoriye product_count ekliyoruz
    qs = Category.objects.annotate(product_count=Count('products'))

    # 2) Arama filtresi
    search = request.GET.get('search', '').strip()
    if search:
        qs = qs.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search)
        )

    # 3) Status filtresi
    status = request.GET.get('status')
    if status == 'active':
        qs = qs.filter(product_count__gt=0)
    elif status == 'inactive':
        qs = qs.filter(product_count=0)

    # 4) Paginasyon (her sayfada 9 kategori)
    paginator = Paginator(qs.order_by('name'), 9)
    categories = paginator.get_page(request.GET.get('page'))

    # 5) Dashboard'daki kartlar için ek sayılar
    total_cats = Category.objects.count()
    active_cats = Category.objects.annotate(product_count=Count('products')).filter(product_count__gt=0).count()
    total_products = Product.objects.count()
    avg_per_cat = total_products / total_cats if total_cats else 0

    return render(request, 'categories/category_list.html', {
        'categories': categories,
        'active_categories_count': active_cats,
        'total_products_count': total_products,
        'avg_products_per_category': round(avg_per_cat, 2),
    })

@login_required
def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        # Debug için:
        print("📝 [Add] POST data:", request.POST)
        print("✅ [Add] form.is_valid():", form.is_valid())
        print("❌ [Add] form.errors:", form.errors)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'Category "{category.name}" has been created successfully.')
            return redirect('category_list')
        else:
            messages.error(request, 'Please fix the errors in the form.')
    else:
        form = CategoryForm()
    return render(request, 'categories/category_form.html', {'form': form})

@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        # Debug için:
        print("📝 [Edit] POST data:", request.POST)
        print("✅ [Edit] form.is_valid():", form.is_valid())
        print("❌ [Edit] form.errors:", form.errors)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'Category "{category.name}" has been updated successfully.')
            return redirect('category_list')
        else:
            messages.error(request, 'Please fix the errors in the form.')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', {'form': form})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    
    if request.method == 'POST':
        name = category.name
        category.delete()
        messages.success(request, f'Category "{name}" has been deleted successfully.')
        return redirect('category_list')
    
    return render(request, 'categories/category_confirm_delete.html', {
        'category': category
    })

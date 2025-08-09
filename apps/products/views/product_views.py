from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from apps.products.models.product import Product
from apps.categories.models.category import Category
from apps.products.forms.product_forms import ProductForm

@login_required
def product_list(request):
    # Filtering
    search = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')
    
    products = Product.objects.all().order_by('id')
    
    if search:
        products = products.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search)
        )
    
    if category_filter:
        products = products.filter(category_id=category_filter)
    
    # Statistics
    total_products = Product.objects.count()
    total_categories = Category.objects.count()
    
    context = {
        'products': products,
        'categories': Category.objects.all(),
        'total_products': total_products,
        'total_categories': total_categories,
    }
    
    return render(request, 'products/product_list.html', context)

@login_required
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Product "{product.name}" has been added successfully.')
            return redirect('product_list')
        else:
            messages.error(request, 'Please fix the errors in the form.')
    else:
        form = ProductForm()
    
    return render(request, 'products/product_form.html', {
        'form': form,
        'title': 'Add New Product'
    })

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Product "{product.name}" has been updated successfully.')
            return redirect('product_list')
        else:
            messages.error(request, 'Please fix the errors in the form.')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'products/product_form.html', {
        'form': form,
        'title': 'Edit Product'
    })

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        product_name = product.name
        product.delete()
        messages.success(request, f'Product "{product_name}" has been deleted successfully.')
        return redirect('product_list')
    
    return render(request, 'products/product_confirm_delete.html', {
        'product': product
    })

# accounts/views.py veya StockManagement/views/user_views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from apps.users.forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from django.db import models

User = get_user_model()

@login_required
def user_list(request):
    # Filtering
    search = request.GET.get('search', '')
    role_filter = request.GET.get('role', '')
    
    users = User.objects.all()
    
    if search:
        users = users.filter(
            models.Q(username__icontains=search) |
            models.Q(first_name__icontains=search) |
            models.Q(last_name__icontains=search) |
            models.Q(email__icontains=search)
        )
    
    if role_filter:
        users = users.filter(role=role_filter)
    
    # Statistics
    total_users = User.objects.count()
    active_users = User.objects.filter(is_active=True).count()
    admin_users = User.objects.filter(role='admin').count()
    manager_users = User.objects.filter(role='manager').count()
    
    context = {
        'users': users,
        'total_users': total_users,
        'active_users': active_users,
        'admin_users': admin_users,
        'manager_users': manager_users,
    }
    
    return render(request, 'users/user_list.html', context)






@login_required
def user_toggle_status(request, pk):
    user = get_object_or_404(User, pk=pk)

    if user == request.user:
        messages.error(request, "You cannot change your own status.")
        return redirect("user_list")

    user.is_active = not user.is_active
    user.save(update_fields=["is_active"])
    status = "active" if user.is_active else "inactive"
    messages.success(request, f"User has been made {status}.")
    return redirect("user_list")



@login_required
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.user == user:
        messages.error(request, "You cannot delete yourself.")
        return redirect("user_list")
    user.delete()
    messages.success(request, "User has been deleted successfully.")
    return redirect("user_list")

@login_required
def user_create(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User has been created successfully.")
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/user_form.html', {'form': form, 'title': 'Add New User'})

@login_required
def user_edit(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User has been updated successfully.")
            return redirect('user_list')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form, 'title': 'Edit User'})


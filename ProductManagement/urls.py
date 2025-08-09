from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# Accounts views
from accounts.views.login_views import login_views, logout_view
from accounts.views.dashboard_views import dashboard_view

# Apps views
from apps.products.views.product_views import product_add, product_list, product_edit, product_delete
from apps.categories.views.category_views import category_list, category_add, category_edit, category_delete
from apps.users.views.user_views import (
    user_list, user_create, user_edit, user_delete, user_toggle_status
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path('',                 login_views,  name='login'),
    # Django'nun hazır login'i kalsın ama ismini değiştirelim ki 'login' adı bize ait olsun
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login_django'),

    # LOGOUT: Custom view (GET/POST serbest) — 405 biter
    path('accounts/logout/', logout_view, name='logout'),

    path('dashboard/',      dashboard_view, name='dashboard'),

    # User management
    path('users/',                     user_list,   name='user_list'),
    path('users/add/',                 user_create, name='user_create'),
    path('users/edit/<int:pk>/',       user_edit,   name='user_edit'),
    path('users/<int:pk>/delete/',     user_delete, name='user_delete'),
    path('users/<int:pk>/toggle-status/', user_toggle_status, name='user_toggle_status'),

    # Product management
    path('products/',                  product_list,   name='product_list'),
    path('products/add/',              product_add,    name='product_add'),
    path('products/edit/<int:pk>/',    product_edit,   name='product_edit'),
    path('products/<int:pk>/delete/',  product_delete, name='product_delete'),

    # Category management
    path('categories/',                category_list,  name='category_list'),
    path('categories/add/',            category_add,   name='category_add'),
    path('categories/<int:pk>/edit/',  category_edit,  name='category_edit'),
    path('categories/<int:pk>/delete/',category_delete,name='category_delete'),

    # Django'nun auth URL'leri (password reset vs.). Bizim logout path'imiz üstte olduğu için onu override eder.
    path('accounts/', include('django.contrib.auth.urls')),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=(
            settings.STATICFILES_DIRS[0]
            if settings.STATICFILES_DIRS
            else settings.STATIC_ROOT
        )
    )

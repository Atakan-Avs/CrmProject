from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods

def login_views(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Başarılı login sonrası dashboard'a yönlendir
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'accounts/login.html')

@require_http_methods(["GET", "POST"])
def logout_view(request):
    # GET veya POST fark etmeksizin çıkış yap ve login sayfasına yönlendir
    logout(request)
    return redirect('login')


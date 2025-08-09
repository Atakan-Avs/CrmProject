from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'accounts/user_detail.html', {'user': user})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

def user_edit_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        # Burada istersen username veya email validasyon ekleyebilirsin
        user.username = username
        user.email = email
        user.save()
        return redirect('user_list')
    return render(request, 'accounts/user_edit.html', {'user': user})

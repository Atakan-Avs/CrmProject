from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def user_list_view(request):
    users = User.objects.all().order_by('id')
    return render(request, 'accounts/user_list.html', {'users': users})

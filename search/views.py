from django.contrib.auth.models import User
from django.shortcuts import render
from .filters import UserFilter

def Search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'user_list.html', {'filter': user_filter})

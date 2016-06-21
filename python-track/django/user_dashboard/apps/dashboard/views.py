from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from ..login_registration.models import User

# Create your views here.
def user_dash(request):
    if User.objects.get(id=request.session['id']).user_level == 9:
        return redirect(reverse('admin-dash'))
    context = {
        'users': User.objects.all()
    }
    return render(request, 'dashboard/dashboard.html', context)

def admin_dash(request):
    if User.objects.get(id=request.session['id']).user_level < 9:
        return redirect(reverse('user-dash'))
    context = {
        'users': User.objects.all()
    }
    return render(request, 'dashboard/admin-dashboard.html', context)

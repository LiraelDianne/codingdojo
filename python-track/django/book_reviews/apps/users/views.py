from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

from .models import User


def index(request):
    return render(request, "index.html")

def user_register(request):
    if request.method == "POST":
        val = User.userManager.register(**request.POST)
        if val[0]:
            user = val[1]
            user = User.objects.create(name=user['name'], alias=user['alias'],
                email=user['email'], password=user['password'])
            request.session['id'] = user.id
            return redirect(reverse('books'))
        else:
            errors = val[1]
            for error_type in errors:
                messages.add_message(request, messages.INFO,
                    errors[error_type], extra_tags=error_type)
            return redirect(reverse('landing'))

def user_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        val = User.userManager.login(email=email, password=password)
        if val[0]:
            user = val[1]
            request.session['id'] = user.id
            return redirect(reverse('books'))
        else:
            errors = val[1]
            for error_type in errors:
                messages.add_message(request, messages.INFO,
                    errors[error_type], extra_tags=error_type)
            return redirect(reverse('landing'))

def user_profile(request, user_id):
    user = User.objects.get(id=request.session['id'])
    context = {
        'user': user,
        'reviews': user.review_set.all(),
        'review_count': user.review_set.count()
    }
    return render(request, 'profile.html', context)

def logout(request):
    request.session.flush()
    return redirect(reverse('landing'))

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

from .models import User

def index(request):
    return render(request, 'login_registration/index.html')

def registerUser(request):
    if request.method == 'POST':
        validate = User.userManager.register(**request.POST)
        if validate[1]:
            user = validate[0]
            User.objects.create(first_name=user['first_name'], last_name=user['last_name'], email=user['email'], password=user['password'])
            request.session['name'] = user['first_name']
            return redirect(reverse('login-reg-success'))
        else:
            errors = validate[0]
            for error_type in errors:
                messages.add_message(request, messages.INFO, errors[error_type], extra_tags=error_type)
            return redirect(reverse('login-reg-index'))

def loginUser(request):
    if request.method == 'POST':
        validate = User.userManager.login(request.POST['email'], request.POST['password'])
        if validate[1]:
            user = validate[0]
            request.session['name'] = user.first_name
            return redirect(reverse('login-reg-success'))
        else:
            errors = validate[0]
            for error_type in errors:
                messages.add_message(request, messages.INFO, errors[error_type], extra_tags=error_type)
            return redirect(reverse('login-reg-index'))

def success(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'login_registration/display.html', context)

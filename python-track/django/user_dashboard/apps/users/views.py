from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

from ..login_registration.models import User

def home_profile(request):
    context = {
        'user': User.objects.get(id=request.session['id'])
    }
    return render(request, 'users/profile.html', context)

def user_profile(request, user_id):
    if user_id == request.session['id']:
        return redirect(reverse('home-profile'))
    context = {
            'user': User.objects.get(id=user_id)
        }
    return render(request, 'users/profile.html', context)

def post_message(request):
    pass

def comment(request):
    pass

def new_user(request):
    if 'id' not in request.session:
        print 'no session id'
        return redirect(reverse('landing'))
    if User.objects.get(id=request.session['id']).user_level == 9:
        return render(request, 'users/new_user.html')
    else:
        print "not admin"

def create_user(request):
    if request.method == 'POST':
        validate = User.userManager.register(**request.POST)
        if validate[1]:
            user = validate[0]
            User.objects.create(first_name=user['first_name'],
                last_name=user['last_name'],
                email=user['email'],
                password=user['password'],
                user_level=user['user_level'])
            request.session['name'] = user['first_name']
            return redirect(reverse('admin-dash'))
        else:
            errors = validate[0]
            for error_type in errors:
                messages.add_message(request, messages.INFO, errors[error_type], extra_tags=error_type)
            return redirect(reverse('create-user'))

def edit_profile(request):
    if 'id' not in request.session:
        return redirect(reverse('landing'))
    context = {
        'user': User.objects.get(id=request.session['id'])
    }
    return render(request, 'users/edit-profile.html', context)

def edit_user(request, user_id):
    if 'id' not in request.session:
        return redirect(reverse('landing'))
    if User.objects.get(id=request.session['id']).user_level == 9:
        context = {
            'user': User.objects.get(id=user_id)
        }
        return render(request, 'users/edit.html', context)
    else:
        return redirect(reverse('user-profile'))

def update_info(request, id):
    # changing methods in controller and model to accept an id parameter separately
    # update templates to remove hidden inputs
    if request.method == "PUT":
        valid = User.userManager.edit(id, **request.PUT)
        if not valid[0]:
            errors = valid[0]
            for error_type in errors:
                messages.add_message(request, messages.INFO, errors[error_type], extra_tags=error_type)
            return redirect(reverse('edit-profile'))

    return redirect(reverse('user-dash'))

def update_pw(request, id):
    if request.method == 'PUT':
        valid = User.userManager.password(id, **request.PUT)
        if not valid[0]:
            errors = valid[0]
            for error_type in errors:
                messages.add_message(request, messages.INFO, errors[error_type], extra_tags=error_type)
            return redirect(reverse('edit-profile'))

def update_desc(request, id):
    if request.method == 'PUT':
        User.objects.get(id=id).description = request.PUT['description']
        return redirect(reverse('user-dash'))
    return redirect(reverse('edit-profile'))

def remove_user(request, id):
    User.objects.get(id=id).delete()
    return redirect(reverse('admin-dash'))

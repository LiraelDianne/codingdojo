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
    else:
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
            User.objects.create(first_name=user['first_name'], last_name=user['last_name'], email=user['email'], password=user['password'])
            request.session['name'] = user['first_name']
            return redirect(reverse('admin-dash'))
        else:
            errors = validate[0]
            for error_type in errors:
                messages.add_message(request, messages.INFO, errors[error_type], extra_tags=error_type)
            return redirect(reverse('create-user'))

def edit_user(request, id):
    if 'id' not in request.session:
        return redirect(reverse('landing'))
    print request.session['id']
    if User.objects.get(id=request.session['id']).user_level == 9:
        context = {
            'user': User.objects.get(id=id)
        }
        return render(request, 'users/edit.html', context)
    else:
        print "not admin"

def update_user(request, id):
    # if request.method == "PUT":
    #     #VALIDATE??
    #     user = user.objects.get(id=request.PUT['id'])
    #     user.first_name = request.PUT['first_name']
    #     user.last_name = request.PUT['last_name']

    return redirect(reverse('admin-dash'))

def update_pw(request, id):
    pass

def remove_user(request, id):
    User.objects.get(id=id).delete()
    return redirect(reverse('admin-dash'))

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from ..login_registration.models import User
from .models import Course

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.order_by('-id')
    }
    return render(request, 'courses/index.html', context)

def add(request):
    if request.method == "POST":
        name, description = request.POST['name'], request.POST['description']
        Course.objects.create(name=name, description=description)
    return redirect(reverse('course-index'))

def confirm(request, id):
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request, 'courses/confirm.html', context)

def delete(request):
    course = Course.objects.get(id=request.POST['id'])
    course.delete()
    return redirect(reverse('course-index'))

def display_users_courses(request):
    context = {
        'courses': Course.objects.all(),
        'users': User.objects.all()
    }
    return render(request, 'courses/users_courses.html', context)

def add_user_course(request):
    if request.method == 'POST':
        course = Course.objects.get(id=request.POST['course'])
        user = User.objects.get(id=request.POST['user'])
        course.users.add(user)
    return redirect(reverse('users-courses'))

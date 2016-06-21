from django.shortcuts import render, redirect

def index(request):
    return render(request, "first_app/index.html")

def show(request):
    print 'running show'
    return render(request, 'first_app/show_users.html')

def create(request):
    if request.method == 'POST':
        print request.POST
        request.session['name'] = request.POST['first_name']
        return redirect('/')
    else:
        return redirect('/')

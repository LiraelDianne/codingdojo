from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def ninjas(request):
    return render(request, 'ninjas.html')

def ninja(request, color):
    context = {
        "color": color
    }
    return render(request, 'ninja.html', context)

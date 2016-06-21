from django.shortcuts import render, redirect
import random
import string

def random_word():
    return "".join(random.choice(string.ascii_uppercase + string.digits) for char in range(14))

def index(request):
    return render(request, 'index.html')

def randomize(request, methods='POST'):
    if request.method == 'POST':
        if 'counter' in request.session:
            request.session['counter'] += 1
        else:
            request.session['counter'] = 1
        request.session['random_word'] = random_word()
        return redirect('/')
    else:
        return redirect('/')

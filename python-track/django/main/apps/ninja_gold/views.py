from django.shortcuts import render, redirect
import random

def index(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
    return render(request, 'index.html')

def process(request, methods="POST"):
    if request.method == 'POST':
        data = request.POST
        if data['building'] == 'farm':
            number = random.randrange(10, 21)
            message_string = "Earned {} golds from the farm!"
        elif data['building'] == 'cave':
            number = random.randrange(5, 10)
            message_string = "Earned {} golds from the cave!"
        elif data['building'] == 'house':
            number = random.randrange(2, 6)
            message_string = "Earned {} golds from the house!"
        if data['building'] == 'casino':
            number = random.randrange(-50, 51)
            if number < 0:
                message_string = "Entered a casino and lost {} golds..ouch."
            else:
                message_string = "Entered a casino and won {} golds."
        request.session['gold'] += number
        if 'log' not in request.session:
            request.session['log'] = []
        request.session['log'].append(message_string.format(number))
    return redirect('/')

def reset(request, methods="POST"):
    request.session.clear()
    return redirect('/')

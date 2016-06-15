from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')

def process(request, methods='POST'):
    if request.method == 'POST':
        if 'count' in request.session:
            request.session['count'] += 1
        else:
            request.session['count'] = 1
        request.session['name'] = request.POST['name']
        request.session['dojo'] = request.POST['dojo']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')
    return redirect('/')

def displayresult(request):
    return render(request, 'result.html')

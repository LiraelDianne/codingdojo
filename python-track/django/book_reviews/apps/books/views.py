from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from ..users.models import User
from .models import Author, Book, Review

# Create your views here.
def index(request):
    context = {
        'user': User.objects.get(id=request.session['id']),
        'reviews': Review.objects.order_by('-created_at')[:3],
        'books': Book.objects.order_by('name')
    }
    return render(request, "books.html", context)

def add_book(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, "add-book.html", context)

def create_book(request):
    if request.method == "POST":
        #create book object and review
        title = request.POST['title']
        if request.POST['new-author']:
            author = Author.objects.create(name=request.POST['new-author'])
        else:
            author = Author.objects.get(request.POST['author-list'])
        book = Book.objects.create(name=title, author=author)
        rating = request.POST['rating']
        user = User.objects.get(id=request.session['id'])
        content = request.POST['content']
        review = Review.objects.create(book=book, rating=rating, user=user,
            content=content)

        return redirect(reverse('display-book', kwargs={'book_id': book.id}))
    else:
        return redirect(reverse('books'))

def display_book(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
        'reviews': Review.objects.filter(book__id=book_id)
    }
    return render(request, 'display-book.html', context)

def add_review(request, book_id):
    if request.method == "POST":
        book = Book.objects.get(id=book_id)
        rating = request.POST['rating']
        user = User.objects.get(id=request.session['id'])
        content = request.POST['content']
        review = Review.objects.create(book=book, rating=rating, user=user,
            content=content)
        return redirect(reverse('display-book', kwargs={'book_id': book.id}))

    return redirect(reverse('display-book', kwargs={'book_id': book_id}))

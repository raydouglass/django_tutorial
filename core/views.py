from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Author, Book


# Create your views here.


def index(request):
    books = Book.objects.all()
    template = loader.get_template('index.html')
    context = {'books': books}
    return HttpResponse(template.render(context, request))


def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book.html', {'book': book})

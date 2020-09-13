from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from core.serializers import AuthorSerializer, BookSerializer

from .models import Author, Book, BookForm


# Create your views here.


def index(request):
    books = Book.objects.all()
    template = loader.get_template('index.html')
    context = {'books': books}
    return HttpResponse(template.render(context, request))


def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book.html', {'book': book})


def book_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return HttpResponseRedirect(f'/{book.id}')
        else:
            raise Exception()
    else:
        form = BookForm

    return render(request, 'form.html', {'form': form})


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-year')
    serializer_class = BookSerializer


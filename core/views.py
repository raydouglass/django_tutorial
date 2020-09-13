from django.http import HttpResponse
from django.template import loader

from .models import Author, Book
# Create your views here.


def index(request):
    books = Book.objects.all()
    template = loader.get_template('index.html')
    context = {'books': books}
    return HttpResponse(template.render(context, request))

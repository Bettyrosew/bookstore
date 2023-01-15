from django.http import HttpResponse
from .models import Book
from django.template import loader
from django.shortcuts import render, get_object_or_404


def home(request):
    """View function for home page of site."""
    book_list = Book.objects.order_by('title')
    num_books = Book.objects.all().count()
    # template = loader.get_template('storecatalog/index.html')
    context = {
        'book_list': book_list,
        'num_books': num_books,
    }
    return HttpResponse(render(request, 'storecatalog/index.html', context))

from django.shortcuts import render
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from .models import Book
from .forms import BookForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = Book.objects.create(
                title = form.cleaned_data.get('title'),
                author = form.cleaned_data.get('author'),
                description = form.cleaned_data.get('description'),
                year = form.cleaned_data.get('year')
            )
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "bookListChanged": None,
                        "showMessage": f"{book.title} added."
                    })
                })
        else:
            return render(request, 'book_form.html', {
                'form': form,
            })
    else:
        form = BookForm()
    return render(request, 'book_form.html', {
        'form': form,
    })

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, initial={
            'title' : book.title,
            'author' : book.author,
            'description' : book.description,
            'year': book.year
        })
        if form.is_valid():
            book.title = form.cleaned_data.get('title')
            book.author = form.cleaned_data.get('author')
            book.description = form.cleaned_data.get('description')
            book.year = form.cleaned_data.get('year')

            book.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "bookListChanged": None,
                        "showMessage": f"{book.title} updated."
                    })
                }
            )
        else:
            return render(request, 'book_form.html', {
                'form': form,
                'book': book,
            })
    else:
        form = BookForm(initial={
            'title' : book.title,
            'author' : book.author,
            'description' : book.description,
            'year': book.year
            })
    return render(request, 'book_form.html', {
        'form': form,
        'book': book,
    })

def remove_book_confirmation(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_delete_confirmation.html', {
        'book': book,
    })

@ require_POST
def remove_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "bookListChanged": None,
                "showMessage": f"{book.title} deleted."
            })
        })
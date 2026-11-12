from django.shortcuts import redirect, render

from .forms import BookForm
from .models import Book


def book_list(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'library/book_list.html', {'books': books})


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', {'form': form})

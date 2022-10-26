from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Author, Genre
from django.views.generic import ListView, DetailView
from cart.forms import CartAddBookForm


def bookshelf(request):
    return render(request, 'bookstore/bookshelf.html', {'title': 'BookShelf'})


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'bookstore/booklist.html'
    context_object_name = 'books'
    paginate_by = 20


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    cart_book_form = CartAddBookForm()

    def book_detail(request, id):
        book = get_object_or_404(Book,
                                    id=id)
        cart_book_form = CartAddBookForm()
        return render(request,
                      'bookstore/book_detail.html',
                      {'book': book,
                       'cart_book_form': cart_book_form})


class AuthorListView(LoginRequiredMixin, ListView):
    model = Author
    template_name = 'bookstore/authorlist.html'
    context_object_name = 'authors'
    paginate_by = 20


class AuthorDetailView(LoginRequiredMixin, DetailView):
    model = Author


class GenreListView(LoginRequiredMixin, ListView):
    model = Genre
    template_name = 'bookstore/genrelist.html'
    context_object_name = 'genres'
    paginate_by = 20


class GenreDetailView(LoginRequiredMixin, DetailView):
    model = Genre

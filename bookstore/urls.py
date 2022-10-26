from django.urls import path
from . import views
from .views import BookListView, BookDetailView, AuthorListView, AuthorDetailView, GenreListView, GenreDetailView


urlpatterns = [
    path('bookshelf/', views.bookshelf, name='bookshelf'),
    path('booklist/', BookListView.as_view(), name='booklist'),
   # path('bookdetail/<int:pk>', BookDetailView.as_view(), name='bookdetail'),
    path('bookdetail/<int:id>', views.BookDetailView.book_detail, name='bookdetail'),
    path('authorlist/', AuthorListView.as_view(), name='authorlist'),
    path('authordetail/<int:pk>', AuthorDetailView.as_view(), name='authordetail'),
    path('genrelist/', GenreListView.as_view(), name='genrelist'),
    path('genredetail/<int:pk>', GenreDetailView.as_view(), name='genredetail'),
]
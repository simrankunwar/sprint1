from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')
    picture = models.ImageField(default='default_genre.jpg', upload_to="genre_pics")
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('genredetail', args=[str(self.id)])

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(default='default_book.jpg', upload_to="book_pics")
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, unique=True,
                             help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    status = models.CharField(max_length=200)

    class Meta:
        ordering = ['title']
        index_together = ('id',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bookdetail', args=[str(self.id)])


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(default='default_author.jpg', upload_to="author_pics")
    bio = models.TextField()

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('authordetail', args=[self.id])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

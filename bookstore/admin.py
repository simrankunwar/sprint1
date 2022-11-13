from django.contrib import admin
from .models import Author, Genre, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'bio')

    fields = ['first_name', 'last_name', 'bio']


admin.site.register(Author, AuthorAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

    fields = ['name', 'description']


admin.site.register(Genre, GenreAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'stock')

    list_editable = ['stock']


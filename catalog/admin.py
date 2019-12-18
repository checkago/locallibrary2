from django.contrib import admin
from .models import Author, Genre, Book, Chapter


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'summary')


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('book', 'name')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Genre, GenreAdmin)


""" """


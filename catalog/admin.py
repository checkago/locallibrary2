from django.forms import ModelForm
from django import forms
from django.contrib import admin
from .models import Author, Genre, Book, CardColor, Publisher
from ckeditor.widgets import CKEditorWidget



class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = [('first_name', 'last_name'), ('date_of_birth', 'date_of_death'), 'image', 'summary']


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_genre', 'summary', 'views')
    list_filter = ['genre']
    exclude = ['views']

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


class CardColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'color',)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(CardColor, CardColorAdmin)
admin.site.register(Publisher, PublisherAdmin)


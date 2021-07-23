from django.forms import ModelForm
from django import forms
from django.contrib import admin
from .models import Author, Genre, Book, Chapter
from ckeditor.widgets import CKEditorWidget


class ChapterAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'))

    class Meta:
        model = Chapter
        fields = '__all__'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = [('first_name', 'last_name'), ('date_of_birth', 'date_of_death')]


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'summary')


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('book', 'name')
    list_filter = ('book',)
    form = ChapterAdminForm


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Genre, GenreAdmin)


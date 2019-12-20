from django.forms import ModelForm
from django.contrib import admin
from .models import Author, Genre, Book, Chapter
from suit_ckeditor.widgets import CKEditorWidget


class ChapterForm(ModelForm):
    class Meta:
        widgets = {
            'text': CKEditorWidget(editor_options={'startupFocus': True})
        }


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'summary')


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('book', 'name')
    list_filter = ('book',)
    form = ChapterForm
    fieldsets = [
        ('Содержимое', {'classes': ('full-width',), 'fields': ('name', 'book', 'text',)})
    ]


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Genre, GenreAdmin)


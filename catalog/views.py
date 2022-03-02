from django.shortcuts import render
from .models import Book, Author, Genre
from django.views import generic


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    genres = Genre.objects.all()
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    # Доступные книги (статус = 'a')
    num_authors = Author.objects.count()  # Метод 'all()' применен по умолчанию.
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_authors': num_authors, 'genres': genres,}
    )


class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        kwargs['author'] = self.get_object().author.all()
        return super(BookDetailView, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author

    def author_detail_view(request, pk):
        try:
            author_id = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404("Книги в каталоге нет")

        # author_id=get_object_or_404(Author, pk=pk)

        return render(
            request,
            'catalog/author_detail.html',
            context={'author': author_id, }
        )


class GenreDetailView(generic.DetailView):
    model = Genre

    def genre_detail(request, pk):
        try:
            genre_id = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            raise Http404("Такого жанра нет")

        return render(request,
                      'catalog/genre_detail.html',
                      context={'genre':genre_id,}
                      )

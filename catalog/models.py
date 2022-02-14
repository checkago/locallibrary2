from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name='Жанр')
    description = models.CharField(max_length=250, verbose_name='Описание жанра')
    color = models.ForeignKey('CardColor', on_delete=models.SET_NULL, null=True, verbose_name='Цвет карточки')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def get_books_count(self):
        return self.books.filter(genre=self).count()

    def get_books(self):
        return self.books.filter(genre=self).all()

    def get_absolute_url(self):
        return reverse('genre_detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='authorb', null=True, verbose_name='Автор')
    image = models.ImageField(upload_to='book_image', verbose_name='Обложка')
    summary = models.TextField(max_length=1000, verbose_name='Описание')
    genre = models.ManyToManyField(Genre, related_name='books', verbose_name='Жанр')
    file = models.FileField(upload_to='book_files', verbose_name='Файл книги')
    paper = models.BooleanField(default=True, verbose_name='Печатная версия книги в ЦБС')
    preview = models.BooleanField(default=False, verbose_name='Ознакомительная версия')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Жанр'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    image = models.ImageField(upload_to='authors_photo', blank=True, verbose_name='Фото автора')
    summary = models.TextField(max_length=400, verbose_name='Описание')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    date_of_death = models.DateField(null=True, blank=True, verbose_name='Дата смерти')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def get_books_count(self):
        return self.authorb.filter(author=self).count()

    def get_books(self):
        return self.authorb.filter(author=self).all()

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)


class CardColor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Цвет')
    color = models.CharField(max_length=50, verbose_name='HTML тег цвета')

    class Meta:
        verbose_name = 'Цвет карточки'
        verbose_name_plural = 'Цвета карточек жанров'

    def __str__(self):
        return self.name
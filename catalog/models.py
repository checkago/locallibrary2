from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name='Жанр')
    description = models.CharField(max_length=250, verbose_name='Описание жанра')
    color = models.CharField(max_length=50, verbose_name='Цвет панели на главной')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def get_books(self):
        return self.books.filter(genre=self).count()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='authorb', null=True, verbose_name='Автор')
    summary = models.TextField(max_length=1000, verbose_name='Описание')
    genre = models.ManyToManyField(Genre, related_name='books', verbose_name='Жанр')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def get_chapters(self):
        return self.chapters.filter(book=self)

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
    summary = models.TextField(max_length=400, verbose_name='Описание')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    date_of_death = models.DateField(null=True, blank=True, verbose_name='Дата смерти')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def get_books(self):
        return self.authorb.filter(author=self).count()

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)


class Chapter(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True, related_name='chapters', verbose_name='Книга')
    text = models.TextField(max_length=99999, verbose_name='Содержимое')

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'

    def __str__(self):
        return self.name
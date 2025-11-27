from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic


# Create your views here.


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')




    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # Метод 'all()' применён по умолчанию.

    num_genres = Genre.objects.count()  # Количество всех жанров

    search = request.GET.get('search', '') # Поиск слова из GET

    
    if search:
        num_books_with_word = Book.objects.filter(
            title__icontains=search
        ).count()
    else:
        num_books_with_word = 0


    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,'search': search,'num_genres': num_genres,'num_books_with_word': num_books_with_word,},
    )

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book


from books.models import Book


class BaseBookMixin:
    queryset = Book.objects.all()
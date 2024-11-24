from books.models import Book
from rest_framework.permissions import IsAuthenticated


class BaseBookMixin:
    queryset = Book.objects.all()


class AuthenticateAPIViewsMixin:
    permission_classes = [IsAuthenticated]
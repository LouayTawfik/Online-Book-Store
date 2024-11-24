import pytest

from books.models import Book
from authentication.models import User
from rest_framework.test import APIClient

@pytest.fixture()
def test_setup():
    user = User.objects.create(username='test_user', password='test_password')
    book = Book.objects.create(title='Test Book', price=20.00)
    yield user, book

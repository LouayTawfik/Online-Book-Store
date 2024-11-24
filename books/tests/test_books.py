from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from unittest.mock import patch
import pytest


client = APIClient()

@pytest.mark.django_db
class TestListBook:
    def test_if_user_is_anonymous_returns_401(self):
        response = client.get(reverse('book_list'))

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestListReview:
    def test_if_user_is_anonymous_returns_401(self):
        response = client.get(reverse('review_list'))

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestCreateReview:
    def test_if_user_is_anonymous_returns_401(self, test_setup):
        user, book = test_setup
        data = {
            'user': user.pk,
            'book': book.pk,
            'rate': 5,
            'review': 'wow'
        }

        response = client.post(reverse('review_list'), data=data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.authenticate')
    def test_submit_review(self, mock_authentication ,test_setup):
        user, book = test_setup
        mock_authentication.return_value = (user, None)
        data = {
            'user': user.pk,
            'book': book.pk,
            'rate': 5,
            'review': 'wow'
        }

        response = client.post(reverse('review_list'), data=data)
        assert response.status_code == status.HTTP_201_CREATED
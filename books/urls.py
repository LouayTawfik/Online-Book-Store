from django.urls import path
from .api import BookListAPIView, BookRetrieveAPIView, ReviewListAPIView

urlpatterns = [
    # books
    path("books/", BookListAPIView.as_view(), name="book_list"),
    path("books/<int:pk>/", BookRetrieveAPIView.as_view(), name="book_detail"),

    # reviews
    path("reviews/", ReviewListAPIView.as_view(), name="review_list"),

]

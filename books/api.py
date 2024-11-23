from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView

from books.mixins import BaseBookMixin
from books.models import Review
from books.serializers import BookListSerializer, BookDetailSerializer, ReviewListSerializer, ReviewSerializer


class BookListAPIView(BaseBookMixin, ListAPIView):
    serializer_class = BookListSerializer


class BookRetrieveAPIView(BaseBookMixin, RetrieveAPIView):
    serializer_class = BookDetailSerializer


class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            self.serializer_class = ReviewSerializer
        return super().get_serializer_class()

from rest_framework import serializers

from books.models import Book, Review


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class BookDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewListSerializer(source='review_book', many=True)
    class Meta:
        model = Book
        fields = '__all__'

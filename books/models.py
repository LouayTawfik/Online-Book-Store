from django.db import models
from django.utils import timezone
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='books')
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='review_user', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='review_book', on_delete=models.CASCADE)
    rate = models.IntegerField()
    review = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user} - {self.book}"

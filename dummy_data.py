import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from books.models import Book

def seed_books(n):
    fake = Faker()
    images = ['1.jpg', '2.jpeg', '3.jpg', '4.jpg', '5.png', '6.jpg', '7.jpg']
    for _ in range(n):
        Book.objects.create(
            title=fake.name(),
            description=fake.text(max_nb_chars=2000),
            author=fake.name(),
            price=round(random.uniform(20.99, 99.99), 2),
            image=f'books/{images[random.randint(0, 6)]}'
        )
    print(f'Seed {n} books successfully!')
seed_books(5)
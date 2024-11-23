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

# def seed_product(n):
#     fake = Faker()
#     images = ['1.jpeg', '2.jpeg', '3.jpeg', '4.jpeg', '5.jpg', '6.jpg', '7.jpeg', '8.jpg', '9.jpg']
#     flags = ['New', 'Sale', 'Feature']
#     for _ in range(n):
#         Product.objects.create(
#             name=fake.name(),
#             image=f'products/{images[random.randint(0, 8)]}',
#             flag= flags[random.randint(0, 2)],
#             price=round(random.uniform(20.99, 99.99), 2),
#             sku=random.randint(1000, 10000000),
#             subtitle=fake.text(max_nb_chars=250),
#             description=fake.text(max_nb_chars=2000),
#             quantity=random.randint(0, 30),
#             brand=Brand.objects.get(id=random.randint(1, 5))
#         )
#     print(f'Seed {n} products successfully!')

# seed_brand(5)
seed_books(5)
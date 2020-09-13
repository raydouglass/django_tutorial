from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from core.models import Author, Book
from datetime import date


class Command(BaseCommand):
    help = 'Adds data to the database'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with transaction.atomic():
            author_1 = Author(first_name='Jennifer', last_name='Fallon')
            author_1.save()

            author_2 = Author(first_name='Ann', last_name='Leckie', birth_date=date(1966, 3, 2))
            author_2.save()

            author_3 = Author(first_name='Sonny', last_name='Whitelaw')
            author_3.save()

            book_1 = Book.objects.create(title='WolfBlade', year=2004)
            book_1.authors.set([author_1])
            book_1.save()

            book_2 = Book.objects.create(title='Ancillary Justice', year=2013)
            book_2.authors.set([author_2])
            book_2.save()

            book_3 = Book.objects.create(title='Stargate SG-1: Roswell', year=2007)
            book_3.authors.set([author_1, author_3])
            book_3.save()


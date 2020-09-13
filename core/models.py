from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Book(models.Model):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author, related_name='books') #related_name is easier than author_set
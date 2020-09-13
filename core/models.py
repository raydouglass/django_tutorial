from django.db import models
from django.forms import ModelForm


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(default=None, null=True, blank=True)

    def __str__(self):
        if self.birth_date:
            return f"{self.first_name} {self.last_name} ({self.birth_date})"
        else:
            return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=128)
    year = models.PositiveIntegerField()
    authors = models.ManyToManyField(Author, related_name='books')  # related_name is easier than author_set

    class Meta:
        unique_together = ['title', 'year']

    def __str__(self):
        return f"{self.title} ({self.year})"


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'year', 'authors']

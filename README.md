# Django Tutorial

1. create skeleton
2. models
    * add app
    * makemigrations
    * migrate
3. add field to model
    * makemigrations - show year issue
4. fake data
    * model changes
    * command
    * `python manage.py create_data`
    
    * `from core.models import Author, Book`
    * `Author.objects.all()`
    * `Author.objects.filter(first_name='Ann')`
    * `Author.objects.filter(books__title='Ancillary Justice')`
    * `Author.objects.filter(first_name='Jennifer')[0].books.all()`

5. root view

6. book view
    * root template changes
    * show 404

7. admin
    * `python manage.py createsuperuser`
    * show admin site

8. book form
9. rest api
    * `pip install django-rest-framework`
    * settings
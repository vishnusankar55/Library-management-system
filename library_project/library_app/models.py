from django.db import models

class Author(models.Model):
    pass

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class BookShelf(models.Model):
    pass

class User(models.Model):
    pass

class History(models.Model):
    pass

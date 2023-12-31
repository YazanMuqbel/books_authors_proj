from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(max_length=255)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    books = models.ManyToManyField('Book', related_name="authors")
    notes = models.TextField(max_length=255)

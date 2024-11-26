from django.db import models

# Create your models here.
#the author model contains the name field 
class Author(models.Model):
    name = models.CharField(max_length=100)
#the book model contains title field, publication_year field and a foreign key to identify the author
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

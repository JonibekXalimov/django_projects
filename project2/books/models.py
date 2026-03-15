from django.db import models

class Book(models.Model):
    title= models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    published_year = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    language = models.CharField(max_length=20)
    genre = models.CharField(max_length=30)

    def __str__(self):
        return f"ID: {self.id} | {self.title}"
    


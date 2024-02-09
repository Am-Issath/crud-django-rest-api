from django.db import models


class Book(models.Model):

    id = models.AutoField(primary_key=True)  # Primary key of the book
    # International Standard Book Number (ISBN) of the book
    ISBN = models.CharField(max_length=50, blank=False, null=False)
    title = models.CharField(max_length=50, blank=False,
                             null=False)  # Title of the book
    # Author(s) of the book
    author = models.CharField(max_length=50, blank=False, null=False)
    publication_date = models.DateField()  # Publication date of the book

    class Meta:
        db_table = "books_db"  # Name of the database table for the Book model

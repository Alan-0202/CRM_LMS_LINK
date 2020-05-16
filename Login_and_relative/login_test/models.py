from django.db import models

# Create your models here.

class BookInfoManager(models.Manager):
    def all(self):
        books = super().all()
        return books

    def create_book(self, btitle, bpub_date):
        model_class = self.model
        book = model_class()
        book.title = btitle
        book.public_date = bpub_date
        book.save()
        return book

class booktest(models.Model):
    title = models.CharField(max_length=20)
    public_date = models.DateField()

    objects = BookInfoManager()


    def __str__(self):
        return self.title

    def ttitle(self):
        return self.title



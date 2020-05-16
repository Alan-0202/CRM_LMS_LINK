from django.db import models

# Create your models here.

class BookInfoManager(models.Manager):
    def all(self):
        books = super().all()
        books = books.filter(isDelete=False)
        return books

    def create_book(self, btitle, bpub_date):
        # book = BookInfo()
        #replance  self.model
        model_class = self.model
        book = model_class()
        book.bittle = btitle
        book.bpub_date = bpub_date
        book.save()
        return book

class BookInfo(models.Model):
    """books model"""
    bittle = models.CharField(max_length=20)

    bpub_date = models.DateField()

    #account of reading
    bread = models.IntegerField(default=0)

    #make a account
    bcommend = models.IntegerField(default=0)

    #whether soft delete
    isDelete = models.BooleanField(default=False)

    objects = BookInfoManager()

class HeroInfo(models.Model):

    hname = models.CharField(max_length=20)

    hgender = models.BooleanField(default=0)

    hcomment = models.CharField(max_length=200)

    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    # whether soft delete
    isDelete = models.BooleanField(default=False)










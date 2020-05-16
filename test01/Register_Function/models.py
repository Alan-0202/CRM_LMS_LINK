from django.db import models

# Create your models here.


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    book_date = models.DateField()

class Hero_list(models.Model):
    """Hero`s name ---> all"""
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=128)

    #the relationship between books and heros


    hbook = models.ForeignKey("BookInfo", on_delete=models.CASCADE)


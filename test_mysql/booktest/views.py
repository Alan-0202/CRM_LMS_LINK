from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from booktest.models import BookInfo
from datetime import date


# Create your views here.

def index(request):
    """show books information"""
    #1. show all the books informations
    books = BookInfo.objects.all()
    #2. usage the templates(fistt step  setting the path of templates)
    return render(request, 'booktest/index.html', {'books':books})

    # return HttpResponse("WangLong_Alan")

def create(request):
    b = BookInfo()
    b.bittle = "LIu Xing HU DIE JIAN"
    b.bpub_date = date(1000,1,1)
    b.save()

    return HttpResponseRedirect('/index')


def delete(request, bid):
    b = BookInfo.objects.get(id = bid)
    b.delete()
    return HttpResponseRedirect('/index')









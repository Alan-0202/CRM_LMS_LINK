from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from login_test.models import booktest
# Create your views here.

def index(request):
    time = datetime.now()
    # return HttpResponse("TIME: %s" %datetime.now())
    return render(request, 'login_test/index.html', {'time':time})

def login(request):

    if request.session.has_key('islogin'):
        return redirect('/index')
    else:
        return render(request, 'login_test/login.html')


def login_check(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    # return HttpResponse(username + "  " + password)
    if username == 'wanglong' and  password == '123':
        response = redirect('/index')
        response.set_cookie('username', username, max_age=7*24*3600)
        request.session['islogin'] = True
        return response
    else:
        return redirect('/login')

def login_check_ajax(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    # return HttpResponse(username + "  " + password)
    if username == 'wanglong' and  password == '123':
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})

def book_list(request):
    books = booktest.objects.all()

    return render(request, 'login_test/list.html')

def prov(request):
    books = booktest.objects.all()
    books_list = []
    for book in books:
        books_list.append((book.title, book.public_date))
    return JsonResponse({'data': books_list})










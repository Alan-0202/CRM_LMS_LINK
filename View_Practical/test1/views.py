from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from test1 import views


# Create your views here.
def index(request):
    return render(request, 'test1/index.html')


def login(request):
    if request.session.has_key('islogin'):
        redirect('index')
    else:
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''

        return render(request, 'test1/login.html',{'username': username})


def login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')



    # if you have choice the REMEMBER ME positised in HTML, means that you have set one cookie date one day!
    if username == 'wanglong' and password == '123':
        response =  redirect('/index')
        if remember == 'on':
            response.set_cookie('username', username,max_age=7*24*3600)
            #Set session check whether user have made login action.
            request.session['islogin'] = True
        return response
    else:
        return redirect('/login')


def ajax_test(request):
    return render(request, 'test1/ajax_test.html')

def ajax_handle(request):

    return JsonResponse({'res': 1})








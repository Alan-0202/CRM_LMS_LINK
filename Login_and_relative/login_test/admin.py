from django.contrib import admin
from login_test.models import booktest
# Register your models here.



class BooktestInfoManager(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'ttitle', 'title']


admin.site.register(booktest, BooktestInfoManager)
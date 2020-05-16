from django.db import models
"""insert the user authentication model of django to user models"""
from django.contrib.auth.models import AbstractUser

"""ji lei"""
from db.base_model import BaseModel
# Create your models here.

class User(AbstractUser, BaseModel):



    class Meta:
        db_table = 'df_user'
        verbose_name = 'User'
        verbose_name_plural = verbose_name


class Address(BaseModel):
    """adress model"""
    user = models.ForeignKey('User', verbose_name='Belong_to_account', on_delete=models.CASCADE)
    receiver = models.CharField(max_length=20, verbose_name='Receiver')
    addr = models.CharField(max_length=256, verbose_name='Receiver_Address')
    zip_code = models.CharField(max_length=6, null=True, verbose_name='Post_Code')
    phone = models.CharField(max_length=11, verbose_name='Phone_Num')
    is_delete = models.BooleanField(default=False, verbose_name='Is_Or_NOt')

    class Meta:
        db_table = 'df_address'
        verbose_name = 'Adress'
        verbose_name_plural = verbose_name

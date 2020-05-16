from django.db import models
from db.base_model import BaseModel


# Create your models here.


class GoodsType(BaseModel):
    """goods models"""
    name = models.CharField(max_length=20, verbose_name='Classification_Name')
    logo = models.CharField(max_length=20, verbose_name='Logo')
    image = models.ImageField(upload_to='type', verbose_name='Goods_Species_Image')

    class Meta:
        db_table = 'df_goods_type'
        verbose_name = 'Goods_Species'
        verbose_name_plural = verbose_name



class GoodsSKU(BaseModel):
    """Goods SKU Models"""
    status_choices = (
        (0, 'Down'),
        (0, 'Online')
    )



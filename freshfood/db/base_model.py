from django.db import models


class BaseModel(models.Model):
    """ji lei"""

    create_time = models.DateField(auto_now_add=True, verbose_name='Create_time')
    update_time = models.DateField(auto_now=True, verbose_name='update_time')
    is_delete = models.BooleanField(default=False, verbose_name='Delete_tog')

    class Meta:
        """illustrate is a abstract models """
        abstract = True


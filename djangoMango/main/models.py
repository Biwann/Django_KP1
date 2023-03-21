from django.db import models


class Numbers(models.Model):
    number = models.IntegerField('Число')

    def __int__(self):
        return self.number

    class Meta:
        verbose_name = 'Number'
        verbose_name_plural = 'Numbers'
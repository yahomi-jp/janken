from django.db import models
from django.db.models.base import Model
from django.conf import settings

# Create your models here.

class Opponent(models.Model):
    name = models.CharField('対戦相手', max_length=12)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作成者', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Opponents'
    
    def __str__(self):
        return self.name

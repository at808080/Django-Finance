from django.db import models

from djongo import models as models_djongo

# Create your models here.

class Stock(models.Model):
    name = models_djongo.CharField(max_length=50)
    ticker = models_djongo.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.name} ({self.ticker})'


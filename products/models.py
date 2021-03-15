from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField(max_length=3500)
class offers(models.Model):
    code=models.CharField(max_length=20)
    description=models.CharField(max_length=500)
    discount=models.FloatField()
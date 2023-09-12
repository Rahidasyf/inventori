from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    kelas = models.CharField(max_length=255)
    menu = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.CharField(max_length=255)
    category = models.TextField()
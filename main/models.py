from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='')
    kelas = models.CharField(max_length=255, default='')
    menu = models.CharField(max_length=255, default ='')
    amount = models.IntegerField()
    description = models.TextField()
    price = models.CharField(max_length=255, default='')
    category = models.TextField()
    date_added = models.DateField(auto_now=True, null = True)
    image = models.CharField(max_length=255, default ='')
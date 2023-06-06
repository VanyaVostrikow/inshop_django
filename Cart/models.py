from django.db import models
from django.contrib.auth import login, logout, authenticate
from Main.models import Product
from django.contrib.auth import get_user_model



class Cart(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='basket')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    num = models.PositiveIntegerField(
        verbose_name='количество', default=0)
    datetime = models.DateTimeField(
        verbose_name='время', auto_now_add=True)
    
# Create your models here.

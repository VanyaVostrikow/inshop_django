from django.db import models
from taggit.managers import TaggableManager


class Product(models.Model):
    logo = models.ImageField(upload_to='media')
    category = models.CharField(max_length=50, null = True)
    VC = models.IntegerField()
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=4096)
    price = models.FloatField()
    tags = TaggableManager()
    def __str__(self):
      
        return self.name
        
    def get_absolute_url(self):
        return f'{self.pk}/'

class Comment(models.Model):
    title = models.TextField(max_length=2048)
    PrProd = models.ForeignKey('Product', on_delete = models.CASCADE, null=True)
    PrUser = models.ForeignKey('auth.user', on_delete = models.CASCADE, null = True) 
    def __str__(self):
      
        return self.title
        

class Order(models.Model):
    prname = models.ForeignKey('Product', on_delete = models.CASCADE, null = True)
    






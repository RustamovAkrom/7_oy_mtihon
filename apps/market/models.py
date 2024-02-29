from django.db import models
from apps.users.models import *
from django.conf import settings

class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Categoriy(AbstractBaseModel):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='categories/')
    def __str__(self): return self.name

    
class Product(AbstractBaseModel):
    image = models.ImageField(upload_to="products/")
    title = models.CharField(max_length=60)
    desciptions = models.TextField()
    price = models.FloatField(default=0)
    count = models.IntegerField(default=0)
    categories = models.ForeignKey(Categoriy, models.CASCADE, 'categories')
    ovner = models.CharField(max_length=48)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, 'products')
    
    def __str__(self) -> str:
        return self.title
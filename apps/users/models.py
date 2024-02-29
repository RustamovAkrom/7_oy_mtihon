from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.market.models import AbstractBaseModel, Product
from django.conf import settings


class Author(AbstractUser):
    avatar = models.ImageField(upload_to='authors/avatar/', null=True, default='authors/avatar/default/user.png')

    class Meta:
        db_table = 'Authors'

class AuthorLike(AbstractBaseModel):
    likes = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='likes',
                              on_delete=models.CASCADE)
    
    @property
    def like_count(self): return self.likes.count

    def __str__(self): return f"{self.likes}"


class AuthorCardMarket(AbstractBaseModel):
    products = models.ForeignKey(Product, models.CASCADE)
    authors = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    proruct_count = models.IntegerField(default=0)

    @property
    def our_products(self):
        return self.product.count()

from django.contrib import admin
from apps.market.models import Product, Categoriy
from apps.users.models import AuthorLike
admin.site.register(Product)
admin.site.register(Categoriy)
admin.site.register(AuthorLike)

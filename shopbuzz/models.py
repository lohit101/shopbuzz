from django.db import models
from django.contrib.auth.models import User
# from user_profile.models import User

# Create your models here.
class Shop(models.Model):
    shop_name = models.CharField(verbose_name="Shop Name", max_length=50, null=True, blank=True, default="Default Shop")
    shop_bio = models.CharField(verbose_name="Shop Bio", max_length=500, null=True, blank=True, default="Default Shop Bio")
    shop_logo = models.CharField(verbose_name="Shop Logo", max_length=50, null=True, blank=True, default="Default Shop Logo")
    shop_owner = models.ForeignKey(User, verbose_name="Shop Owner", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.shop_name

class Product(models.Model):
    CATEGORIES = [
        ('Beauty & Health', 'Beauty & Health'),
        ('Electronics', 'Electronics'),
        ('Accessories', 'Accessories'),
        ('Clothing', 'Clothing'),
    ]
    prod_name = models.CharField(verbose_name="Product Name", max_length=50, null=True, blank=True, default="Default Shop")
    prod_bio = models.CharField(verbose_name="Product Bio", max_length=500, null=True, blank=True, default="Default Shop Bio")
    prod_owner = models.ForeignKey(Shop, verbose_name="Shop Name", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.prod_name
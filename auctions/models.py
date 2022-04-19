from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
    CATEGORY_CHOICES = [
        ('FS', 'Fashion'),
        ('TY', 'Toys'),
        ('ET', 'Electronics'),
        ('HM', 'Home')
    ]
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    startingBid = models.DecimalField(max_digits=8, decimal_places=2)
    currentPrice = models.DecimalField(max_digits=8, decimal_places=2)
    imageUrl = models.ImageField(upload_to='img', blank=True)
    category = models.CharField(max_length=2, blank=True, choices=CATEGORY_CHOICES)


class Biding(models.Model):
    bider = models.ForeignKey(User, on_delete=models.CASCADE)
    bidPrice = models.DecimalField(max_digits=8, decimal_places=2)


class Comments(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    desciption = models.CharField(max_length=128)


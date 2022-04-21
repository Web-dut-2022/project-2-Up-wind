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
    image = models.ImageField(upload_to='img', blank=True)
    category = models.CharField(max_length=2, blank=True, choices=CATEGORY_CHOICES)
    listedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    isActive = models.BooleanField()


class Biding(models.Model):
    bid = models.DecimalField(max_digits=8, decimal_places=2)
    bider = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Listing, on_delete=models.CASCADE)


class Comments(models.Model):
    comment = models.CharField(max_length=128)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Listing, on_delete=models.CASCADE)


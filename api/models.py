from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Abstracted model for timestamp for created_at and updated_at
class AbstractDateTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Category Model
class Category(AbstractDateTimeModel):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']


# User Model
class User(AbstractUser, AbstractDateTimeModel):
    categories = models.ManyToManyField(Category, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['created_at']


# Store Model
class Store(AbstractDateTimeModel):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']


# Product Model
class Product(AbstractDateTimeModel):
    name = models.CharField(max_length=100)
    store = models.ForeignKey(Store, related_name='products', blank=True, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']


# Purchase Model
class Purchase(AbstractDateTimeModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='users')

    class Meta:
        ordering = ['created_at']


# Purchase Details Model
class PurchaseDetail(AbstractDateTimeModel):
    purchase = models.ForeignKey(Purchase, on_delete=models.DO_NOTHING, related_name='purchase_details')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()

    class Meta:
        ordering = ['created_at']

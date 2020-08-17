from django.contrib import admin
from api.models import Category, Store, User, Product, Purchase, PurchaseDetail
# Register your models here.

admin.site.register(Category)
admin.site.register(Store)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(PurchaseDetail)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import authentication, permissions
# from django.contrib.auth.models import User
from api.models import Store, Purchase, User, Product
from api.serializers import StoreSerializer, PurchaseSerializer, UserSerializer, ProductSerializer


# Store Create View
class StoreCreateView(generics.CreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


# Store Retrieve View
class StoreRetrieveView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


# Purchase Create View
class PurchaseCreateView(generics.CreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


# Purchase Retrieve View
class PurchaseRetrieveView(generics.RetrieveAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


# User Create View
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# User Retrieve View
class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




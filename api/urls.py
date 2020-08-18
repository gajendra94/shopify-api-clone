from django.urls import path

from .views import StoreCreateView, StoreRetrieveView, PurchaseCreateView, PurchaseRetrieveView, UserCreateView, \
    UserRetrieveView

urlpatterns = [
    path('stores/', StoreCreateView.as_view()),
    path('stores/<int:pk>/', StoreRetrieveView.as_view()),
    path('purchases/', PurchaseCreateView.as_view()),
    path('purchases/<int:pk>/', PurchaseRetrieveView.as_view()),
    path('users/', UserCreateView.as_view()),
    path('users/<int:pk>/', UserRetrieveView.as_view())
]

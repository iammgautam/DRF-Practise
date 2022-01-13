from django.urls import path
from rest_framework import routers
from piggybank.views import CategoryModelViewSet, CurrencyListAPIView, TransactionModelViewSet

router = routers.SimpleRouter()
router.register(r'categories', CategoryModelViewSet, basename='category')
router.register(r'transactions', TransactionModelViewSet, basename='transactions')

urlpatterns = [
    path('', CurrencyListAPIView.as_view(), name= 'currency-list')
] + router.urls

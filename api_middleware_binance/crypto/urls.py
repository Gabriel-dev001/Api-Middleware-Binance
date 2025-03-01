from django.urls import path
from .views import get_crypto_price

urlpatterns = [
    path('historical-price/', get_crypto_price, name='historical-price'),
]

"""shop url"""

from django.urls import path
from .views import home,product

app_name="shop"

urlpatterns = [
    path('', home,name="home"),
    path('', product,name="product"),
]

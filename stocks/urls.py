from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="stocks-home"),
    path('stock/', views.stock, name="stocks-stock"),
]

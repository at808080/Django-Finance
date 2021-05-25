from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="stocks-home"),
    path('stock/', views.stock, name="stocks-stock"),
    path('watchlist/', views.watchlist, name="stocks-watchlist")
]

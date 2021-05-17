from django.shortcuts import render
from django.http import HttpResponse
from .utils.stock import Stock
# Create your views here.

def home(request):
    tesla = Stock("Tesla", "TSLA")
    stocks = [tesla]
    context = {'stocks' : stocks}
    return render(request, 'stocks/home.html', context)


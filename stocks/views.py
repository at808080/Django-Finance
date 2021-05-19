from django.shortcuts import render
from django.http import HttpResponse
from .utils.stock import Stock
# Create your views here.

def home(request):
    tesla = Stock("Tesla", "TSLA")
    dates = []
    closes = []
    prices = tesla.getPrices()
    for date in prices.index:
        dates.append(str(date))
        closes.append(prices['Close'][date])
    context = {'stock' : tesla, 'description' : tesla.getInfoFromTicker('longBusinessSummary'), 'labels' : dates, 'data' : closes}
    return render(request, 'stocks/home.html', context)


from django.shortcuts import render
from django.http import HttpResponse
from .utils.stock import Stock
from .models import Stock as StockModel
# Create your views here.

def home(request):
    stocks = []
    for stock in StockModel.objects.all():
        stocks.append(Stock(stock.name, stock.ticker))
    print(request.user)
    print(request.user.profile)
    print(request.user.profile.stocks)
    context = {'stocks' : stocks}
    return render(request, 'stocks/home.html', context)



def stock(request):
    '''
    stocks = []
    for stock in StockModel.objects.all():
        stock_object = Stock(stock.name, stock.ticker)
        dates_ = []
        closes_ = []
        prices_ = stock_object.getPrices()
        for date in prices_.index:
            dates_.append(str(date))
            closes_.append(prices_['Close'][date])
    print(stocks)
    stocks2 = request.user.profile.stocks.all()
    print(stocks2)
    '''

    tesla = Stock("Tesla", "TSLA")
    dates = []
    closes = []
    prices = tesla.getPrices()
    for date in prices.index:
        dates.append(str(date))
        closes.append(prices['Close'][date])
    context = {'stock' : tesla, 'description' : tesla.getInfoFromTicker('longBusinessSummary'), 'labels' : dates, 'data' : closes}
    return render(request, 'stocks/stock.html', context)


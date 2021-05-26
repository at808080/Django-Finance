from django.shortcuts import render
from django.http import HttpResponse
from .utils.stock import Stock
from .models import Stock as StockModel

#finance
import numpy as np
import pandas as pd
# Create your views here.

def home(request):
    stocks = []
    for stock in StockModel.objects.all():
        stock_ = Stock(stock.name, stock.ticker)
        stock_.setDBID(stock.id)
        stocks.append(stock_)
        
    '''
    print(request.user)
    print(request.user.profile)
    print(request.user.profile.stocks)
    '''
    context = {'stocks' : stocks}
    return render(request, 'stocks/home.html', context)

def watchlist(request):
    stocks = [] 
    urls = {}
    for stock in (str(request.user.profile.stocks).split(";")[:-1]):
        stock_ = Stock(StockModel.objects.filter(ticker=stock).first().name, stock)
        stock_.setDBID(StockModel.objects.filter(ticker=stock).first().id)
        stocks.append(stock_)
        urls[str(stock_.ticker)] = "stock/" + str(StockModel.objects.filter(ticker=stock).first().id) + "/"
   
    context = {'stocks' : stocks, 
               'urls' : urls}
    
    return render(request, 'stocks/watchlist.html', context)



def stock(request, id):
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
    #print(str(request.user.profile.stocks).split(";")[:-1])
    stock = StockModel.objects.get(id = id)
    stock_object = Stock(stock.name, stock.ticker)

    '''
    STOCK PRICES
    '''
    dates = []
    closes = []
    prices = stock_object.getPrices()
    print(prices.head())
    for date in prices.index:
        dates.append(str(date))
        closes.append(prices['Close'][date])

    '''
    VOLATILITY
    '''
    relative_absolute_true_range = []
    highs = prices['High']
    lows = prices['Low']
    previous_closes = prices['Close'].shift() #pandas.DataFrame.shift() moves index using default value of 1 to take the previous day's close
    high_minus_low = highs - lows
    highs_minus_closes = np.abs(highs - previous_closes)
    lows_minus_closes = np.abs(lows - previous_closes)
    absolutes = pd.concat([high_minus_low, highs_minus_closes, lows_minus_closes], axis=1)
    #true range
    tr = np.max(absolutes, axis=1)
    #absolute true range
    atr = pd.DataFrame(data=tr.rolling(14).sum()/14, index=prices.index) #rolling applies a function to a rolling window (in this case sum to a window of length 14) and returns a new dataframe with the result

    print(type(atr))
    atr.columns=['ATR']
    atr.fillna(0) #set NaN rows missed during the rolling window sum to zero
    for date in atr.index:
        #print('test ' + str(type(date)) + ' ' + str(type(atr.index[0])))
        if date not in atr.index:
            print(str(date) + ' not in index...')
        else:
            relative_absolute_true_range.append(str(100*atr['ATR'][date]/previous_closes.iloc[-1])) #calculate the relative ATR by dividing by most recent stock price close

    closes2 = []
    for c in closes:
        closes2.append(c*-1)
    #print(str(len(absolute_true_range)) + ' ' + str(len(dates)))
    '''
    BUILD CONTEXT AND RETURN
    '''
    context = {'stock' : stock_object, 
              'description' : stock_object.getInfoFromTicker('longBusinessSummary'), 
              'labels' : dates, 
              'data' : closes,
              'atr' : relative_absolute_true_range}
    return render(request, 'stocks/stock.html', context)


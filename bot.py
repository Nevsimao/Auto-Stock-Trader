import config

import robin_stocks as r # API

import datetime as dt
import time

#login
def login(days):
    time_logged_in = 60*60*24*days
    r.authentication.login(
        username = config.USERNAME,
        password = config.PASSWORD,
        expiresIn = time_logged_in,
        scope = 'internal',
        by_sms = True,
        store_session = True
        )

#logout
def logout():
    r.authentication.logout()

#get stocks
def get_stocks():
    stocks = list()
    stocks.append('TSLA')
    stocks.append('ARKK')
    stocks.append('ARKF')
    return(stocks)

#open market
def open_market():
    market = False
    time_now = dt.datetime.now().time()

    market_open = dt.time(9,30,0)
    market_close = dt.time(15,59,0)

    if time_now > market_open and time_now < market_close:
        market = True
    else:
        print('Market is closed')
    
    return(market)

open_market()

import config

import robin_stocks as r # API

import datetime as dt
import time as t

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


import matplotlib.pyplot as plt
import datetime
import yfinance as yf
import pandas_datareader.data as web


def plot_rub_usd():
    yf.pdr_override()
    df = web.DataReader("USDRUB=X", datetime.datetime.today() - datetime.timedelta(days=365))
    plt.plot(df.index, df["Close"])
    plt.show()


def plot_usd_btc():
    yf.pdr_override()
    df = web.DataReader("BTC-USD", datetime.datetime.today() - datetime.timedelta(days=365))
    plt.plot(df.index, df["Close"])
    plt.show()

def plot_usd_yen():
    yf.pdr_override()
    df = web.DataReader("USDJPY=X", datetime.datetime.today() - datetime.timedelta(days=365))
    plt.plot(df.index, df["Close"])
    plt.show()
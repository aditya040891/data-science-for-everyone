import pandas as pd
import yfinance as yf

from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Select, DataTable, TableColumn
from bokeh.layout import column, row
from bokeh.plotting import figure

DEFAULT_TICKERS = ['AAPL', 'GOOG', 'MSFT', 'NFLX', 'TSLA']
START, END = "2018-01-01", "2021-01-01"


def load_ticker(tickers):
    df = yf.download(tickers, start=START, end=END)
    return df["Close"].dropna()


static_data = load_ticker(DEFAULT_TICKERS)


def get_data(d, t1, t2):
    df = d[[t1, t2]]
    returns = df.pct_change().add_suffix("_returns")
    df = pd.concat([df, returns], axis=1)
    df.rename(columns={t1:"t1", 
                        t2:"t2", 
                        t1 + "_returns":"t1_returns",
                        t2 + "_returns": "t2_returns"})
    return df.dropna()


tickers1 = Select(value="AAPL")








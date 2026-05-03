import yfinance as yf
import pandas as pd
import numpy as np

from bokeh.layouts import row
from bokeh.plotting import figure, show
from bokeh.palettes import Category10_4

tickers = ["AAPL", "GOOG", "IBM", "MSFT"]
data = yf.download(tickers, period='max')
data = data.dropna()['Close']
data = data.reset_index()

p1 = figure(x_axis_type="datetime", 
            title="Adjust Close Stock Prices")

p1.grid.grid_line_alpha = 0.3
p1.xaxis.axis_label = "Date"
p1.yaxis.axis_label = "Price"

for i, tick in enumerate(tickers):
    p1.line(data['Date'], data[tick], color=Category10_4[i], legend_label=tick)

p1.legend.location = "top_left"

window_size = 30
window = np.ones(window_size)/float(window_size)
mv_avg = np.convolve(data['GOOG'], window, 'same')

p2 = figure(x_axis_type="datetime", title="GOOG 30 Day MA")
p2.grid.grid_line_alpha = 0
p2.xaxis.axis_label = "Date"
p2.yaxis.axis_label = "Price"
p2.ygrid.band_fill_color = "blue"
p2.ygrid.band_fill_alpha = 0.1

p2.circle(data['Date'], 
          data['GOOG'], 
          size=4, 
          legend_label="Close",
          color="firebrick",
          alpha=0.2)

p2.line(data['Date'], 
        mv_avg, 
        legend_label="Moving Average",
        color="navy")

p2.legend.location = "top_left"


show(row(p1, p2))


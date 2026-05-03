import yfinance as yf
import pandas as pd
import numpy as np

from bokeh.plotting import figure, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, RangeTool

# Data
data = yf.download('SPY', period='max', auto_adjust=True)

data = data.droplevel(1, axis=1)
data.reset_index(inplace=True)

dates = np.array(data['Date'])

source = ColumnDataSource(data=data)

p = figure(height=300, 
           width=1000,
           tools="xpan",
           toolbar_location=None,
           x_axis_type="datetime",
           x_axis_location="above",
           x_range=(dates[1500], dates[2500]))
            
p.line('Date', 'Close', source=source)

p.yaxis.axis_label = 'Price'

select = figure(title="Drag the middle and edges of the Selection Box to Change The Range", 
                height=150,
                width=1000,
                y_range=p.y_range,
                x_axis_type="datetime",
                tools="",
                toolbar_location=None)

range_tool = RangeTool(x_range=p.x_range)
range_tool.overlay.fill_color="navy"
range_tool.overlay.fill_alpha=0.2

select.line('Date', 'Close', source=source)
select.ygrid.grid_line_color = None
select.add_tools(range_tool)
# select.toolbar.active_drag = range_tool

show(column(p, select))
                

                
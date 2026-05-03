import numpy as np
from flask import Flask, jsonify, make_response, request

from bokeh.models import AjaxDataSource, CustomJS
from bokeh.plotting import figure, show

from threading import Thread

# Bokeh code

adapter = CustomJS(
        code = """
        const result = {x: [], y: []};
        const {points} = cb_data.response;
        for (const [x, y] of points) {
                result.x.push(x);
                result.y.push(y);
        }
        return result;
        """
    )

source = AjaxDataSource(data_url="http://localhost:6060/data/",
                        polling_interval=100,
                        adapter=adapter)

p = figure(height=800,
           width=1000,
           background_fill_color="lightblue",
           title="Streaming Data with Ajax")

p.circle('x', 'y', source=source, size=6)

p.x_range.follow = "end"
p.x_range.follow_interval = 10

# Flask Code

app = Flask(__name__)

def crossdomain(f):
    def wrapped_function(*args, **kwargs):
        resp = make_response(f(*args, **kwargs))
        h = resp.headers
        h['Access-Control-Allow-Origin'] = '*'
        h['Access-Control-Allow-Methods'] = 'GET, OPTIONS, POST'
        h['Access-Control-Allow-Max-Age'] = str(21600)
        requested_headers = request.headers.get('Access-Control-Request-Headers')
        if requested_headers:
            h['Access-Control-Allow-Headers'] = requested_headers
        return resp
    return wrapped_function


# Simulated Stock Data

np.random.seed(42)

x = list(np.arange(0, 6, 0.1))

y = list(np.sin(x) + np.random.random(len(x)))
# y = list(np.cumsum(y))


@app.route('/data/', methods=['GET', 'OPTIONS', 'POST'])
@crossdomain
def data():
    x.append(x[-1]+0.1)
    y.append(np.sin(x[-1] + np.random.random()))
    return jsonify(points=list(zip(x, y)))


def run_app():
    app.run(port=6060)
    
    
Thread(target=run_app).start()

show(p)





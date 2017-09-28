import pandas as pd
import plotly as plotly
import plotly.plotly as py
from plotly.graph_objs import *
plotly.tools.set_credentials_file(username='adamgobes', api_key='suTo9wFs2dMg6XmOnbW3')


df = pd.read_csv('grad-students.csv');
print(df.head());

def multiply_by_100(n):
    return n * 100;

unemployment_rates = map(multiply_by_100, df['Grad_unemployment_rate'].values)





trace = {
  "x": df['Grad_median'].values,
  "y": df['Grad_share'].values,
  "hoverinfo": "text",
  "marker": {
    "color": unemployment_rates,
    "colorbar": {
        "thickness": 15,
        "title": "Unemployment Rate",
        "titleside": "right",
        "xanchor": "left"

    },
    "size": df['Grad_total'].values,
    "sizemode": "area",
    "sizeref": 1000
  },
  "mode": "markers",
  "text": df['Major'].values,
  "type": "scatter"
}
data = Data([trace])
layout = {
  "height": 650,
  "hovermode": "closest",
  "margin": {
    "r": 5,
    "t": 40,
    "b": 35,
    "l": 45
  },
  "showlegend": False,
  "title": "Gender, Size, Cash, Unemployment",
  "titlefont": {"size": 16},
  "width": 650,
  "xaxis": {
    "showgrid": False,
    "zeroline": True,
    "title": "Median Salary",
    "showline": True
  },
  "yaxis": {
    "showgrid": False,
    "zeroline": True,
    "title": "Share of Women",
    "showline": True
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename="node-example")

import plotly.graph_objs as go
from plotly.subplots import make_subplots


fig = make_subplots(rows=2, cols=2)
diag1 = go.Bar(x=['a', 'b', 'c', 'd'], y=[4, 2, 5, 1])
diag2 = go.Bar(x=['Nana', 'Klara'], y=[4, 2])
diag3 = go.Scatter(x=[2, 4,  3], y=[1, 5, 3])
diag4 = go.Pie(labels=['a', 'b'], values=[1, 2])
fig.append_trace(diag1, 1, 1)
fig.append_trace(diag2, 2, 2)
fig.append_trace(diag3, 2, 1)
fig.write_html('test.html', auto_open=True)

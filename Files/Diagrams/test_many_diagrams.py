import plotly.graph_objs as go
from plotly.subplots import make_subplots


fig = make_subplots(2, 2)

diag1 = go.Bar(x=['Alex', 'Misha', 'Alina', 'Alyona'], y=[11, 5, 3, 7], name='first')
diag2 = go.Scatter(x=[1, 5, 3, 7, 4], y=[7, 3, 6, 2, 3], name='second')

fig.append_trace(diag1, 2, 2)
fig.append_trace(diag2, 1, 1)

fig.write_html('test.html', auto_open=True)

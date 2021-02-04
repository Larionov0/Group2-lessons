import plotly.graph_objs as go


x1 = [1, 2, 4]
y1 = [1, 3, -1]

x2 = [0, 4, 6]
y2 = [-3, 5, 5]


diag1 = go.Scatter(x=x1, y=y1)  # 2d площина
diag2 = go.Scatter(x=x2, y=y2)
fig = go.Figure(data=[diag1, diag2])
fig.write_html('d3.html', auto_open=True)

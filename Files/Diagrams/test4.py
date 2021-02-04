import plotly.graph_objs as go


def y(x):
    return 2 * x - 3


def g(x):
    return 2 * x ** 2


x_list = []
y_list = []

x = -10
while x <= 10:
    y_value = y(x)
    x_list.append(x)
    y_list.append(y_value)
    x += 1


x_list2 = []
g_list = []

x = -10
while x <= 10:
    g_value = g(x)
    x_list2.append(x)
    g_list.append(g_value)
    x += 1


diag1 = go.Scatter(x=x_list, y=y_list)
diag2 = go.Scatter(x=x_list2, y=g_list)
fig = go.Figure(data=[diag1, diag2])
fig.write_html('d4.html', auto_open=True)

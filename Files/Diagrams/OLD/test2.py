import plotly.graph_objs as go


names = ['Бомонія', 'Корелія', 'Апунія', 'Нокіа', 'Кратія']
squares = [12847, 6244, 235, 22667, 8000]


diag = go.Pie(labels=names, values=squares)  # кругова діаграма
fig = go.Figure(data=[diag])
fig.write_html('d2.html', auto_open=True)

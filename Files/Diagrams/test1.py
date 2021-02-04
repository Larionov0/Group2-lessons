import plotly.graph_objs as go


names = ['Sasha', 'Bob', 'Katia', 'Alina', 'Petya']
marks = [10, 12, 4, 8, 6]

diag = go.Bar(x=names, y=marks)  # гістограма (стовпчикова)
figure = go.Figure(data=[diag])
figure.write_html('d1.html', auto_open=True)

import plotly.graph_objs as go
from plotly.subplots import make_subplots

specs = [[{'type': 'domain'}, {'type': 'domain'}], [{'type': 'domain'}, {'type': 'domain'}]]

dict_counter_of_all = {}

names = []
platforms_number = []
ratings = []
playtime = []
number_of_owners = []

i = 0
with open("steam.csv", encoding='utf-8') as file:
    headers = file.readline()
    clean_headers = headers.rstrip().split(',')

    for line in file:
        if i < 30:
            game_list = line.rstrip().split(',')
            names.append(game_list[clean_headers.index("name")])

            all_platforms = game_list[clean_headers.index("platforms")]
            number_of_platforms = len(all_platforms.split(";"))
            platforms_number.append(number_of_platforms)

            positive_ratings = game_list[clean_headers.index("positive_ratings")]
            ratings.append(positive_ratings)

            average_playtime = game_list[clean_headers.index("average_playtime")]
            playtime.append(average_playtime)

            owners = game_list[clean_headers.index("owners")]
            max_owners = owners.split("-")[1]
            number_of_owners.append(max_owners)

        i += 1

fig = make_subplots(rows=2, cols=2, specs=specs)

fig.add_trace(go.Pie(labels=names, values=platforms_number), 1, 1)
fig.add_trace(go.Pie(labels=names, values=ratings), 1, 2)
fig.add_trace(go.Pie(labels=names, values=playtime), 2, 1)
fig.add_trace(go.Pie(labels=names, values=number_of_owners), 2, 2)

fig = go.Figure(fig)
fig.write_html('task1.html', auto_open=True)

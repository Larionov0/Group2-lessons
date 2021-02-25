import plotly.graph_objs as go
from plotly.subplots import make_subplots

specs = [[{'type': 'domain'}, {'type': 'domain'}], [{'type': 'domain'}, {'type': 'domain'}]]


def task(string):
    things_count = {}

    i = 0
    with open("steam.csv", encoding='utf-8') as file:
        headers = file.readline()
        clean_headers = headers.rstrip().split(',')
        for line in file:
            if i < 10:
                game_list = line.rstrip().split(',')
                if ";" in game_list[clean_headers.index(string)]:
                    all_things = game_list[clean_headers.index(string)]
                    number_of_things = len(all_things.split(";"))
                    things_count[game_list[1]] = number_of_things
                elif "-" in game_list[clean_headers.index(string)]:
                    all_things = game_list[clean_headers.index(string)]
                    number_of_things = all_things.split("-")
                    things_count[game_list[1]] = (int(number_of_things[1]) - int(number_of_things[0])) / 2
                else:
                    things_count[game_list[1]] = game_list[clean_headers.index(string)]
            i += 1
        names = list(things_count.keys())
        counts = list(things_count.values())

    return names, counts


fig = make_subplots(rows=2, cols=2, specs=specs)

task1 = task("platforms")
fig.add_trace(go.Pie(labels=task1[0], values=task1[1]), 1, 1)

task2 = task("positive_ratings")
fig.add_trace(go.Pie(labels=task2[0], values=task2[1]), 1, 2)

task3 = task("average_playtime")
fig.add_trace(go.Pie(labels=task3[0], values=task3[1]), 2, 1)

task4 = task("owners")
fig.add_trace(go.Pie(labels=task4[0], values=task4[1]), 2, 2)

fig = go.Figure(fig)
fig.write_html('task1.html', auto_open=True)

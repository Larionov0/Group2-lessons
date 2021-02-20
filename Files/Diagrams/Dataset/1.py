import plotly.graph_objs as go
import time


def build_graphic(developers, counts):
    diag = go.Pie(labels=developers, values=counts)
    fig = go.Figure(data=[diag])
    fig.write_html('task1.html', auto_open=True)


def get_developers_counts_from_file(filename='steam.csv'):
    dev_index = 4

    developers_counts = {}

    with open(filename, encoding='utf-8') as file:
        headers = file.readline()
        for line in file:
            game_list = line.rstrip().split(',')
            developer_name = game_list[dev_index]

            if developer_name in developers_counts:
                developers_counts[developer_name] += 1
            else:
                developers_counts[developer_name] = 1

    return developers_counts


def filter_first_n_developers_by_counts(developers_counts, n=25):
    """
    :return: developers, counts  (first n)
    """
    developers = list(developers_counts.keys())
    counts = list(developers_counts.values())

    ogr = len(counts) - 1
    while ogr > len(counts) - n - 1:
        i = 0
        while i < ogr:
            if counts[i] > counts[i + 1]:
                counts[i], counts[i + 1] = counts[i + 1], counts[i]
                developers[i], developers[i + 1] = developers[i + 1], developers[i]
            i += 1
        ogr -= 1
    return developers[-n:], counts[-n:]


def task1():
    developers_counts = get_developers_counts_from_file()
    developers, counts = filter_first_n_developers_by_counts(developers_counts)
    build_graphic(developers, counts)


t1 = time.time()
task1()
t2 = time.time()

print(t2 - t1)

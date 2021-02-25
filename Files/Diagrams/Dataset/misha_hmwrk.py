import plotly.graph_objs as go
from plotly.subplots import make_subplots


def find_games(games_lst_need_find):
    '''
    return:

        games_lst[{game_name: str(Gta SA),
            platforms: lst[PC],
            positive_ratings: int(9999),
            average_playtime: int(213),
            owners: 123-123}
            {},
            {}]
    '''
    name_id = 1
    platform_id = 6
    positive_ratings_id = 12
    average_playtime_id = 14
    owners_id = 16

    with open('steam.csv', 'rt', encoding='utf-8') as file:
        headers = file.readline()
        games_lst = []
        for line in file:
            game_lst = line.rstrip().split(',')
            for game_name in games_lst_need_find:

                if game_name == game_lst[name_id]:
                    dct = {}
                    dct['game_name'] = game_lst[name_id]
                    dct['platforms'] = game_lst[platform_id].split(';')
                    dct['positive_ratings'] = game_lst[positive_ratings_id]
                    dct['average_playtime'] = game_lst[average_playtime_id]
                    dct['owners'] = game_lst[owners_id]

                    games_lst.append(dct)
    return games_lst


def find_platforms_num(games_lst):
    '''
    return: list of number platforms
    '''
    lst_platforms = []
    for game in games_lst:
        num = len(game['platforms'])
        lst_platforms.append(int(num))
    return lst_platforms


def positive_ratings(games_lst):
    positive_ratings_lst = []
    for game in games_lst:
        positive_ratings_lst.append(int(game['positive_ratings']))
    return positive_ratings_lst


def average_playtime(games_lst):
    average_playtime_lst = []
    for game in games_lst:
        average_playtime_lst.append(int(game['average_playtime']))
    return average_playtime_lst


def owners(games_lst):
    owners_lst = []
    for game in games_lst:
        temp_lst = game['owners'].split('-')
        num = int(temp_lst[1]) - int(temp_lst[0])
        owners_lst.append(num)
    return owners_lst


def build_diagrams(names_lst, platforms_num_lst, positive_ratings_lst, average_playtime_lst, owners_lst):
    fig = make_subplots(2, 2)

    diag1 = go.Bar(x=names_lst, y=platforms_num_lst, name='platforms')
    diag2 = go.Bar(x=names_lst, y=positive_ratings_lst, name='positive ratings')
    diag3 = go.Bar(x=names_lst, y=average_playtime_lst, name='average playtime')
    diag4 = go.Bar(x=names_lst, y=owners_lst, name='owners')

    fig.append_trace(diag1, 2, 2)
    fig.append_trace(diag2, 1, 1)
    fig.append_trace(diag3, 1, 2)
    fig.append_trace(diag4, 2, 1)

    fig.write_html('test.html', auto_open=True)


def names_lst(games_lst):
    names_lst = []
    for game in games_lst:
        names_lst.append(game['game_name'])
    return names_lst


games_lst_need_find = ['Counter-Strike', 'Counter-Strike: Global Offensive', 'Left 4 Dead',
                       'S.T.A.L.K.E.R.: Shadow of Chernobyl',
                       'Cossacks: Back to War', 'BioShock Infinite', 'DOOM 3', 'Grand Theft Auto: San Andreas']

games_lst = find_games(games_lst_need_find)

platforms_num_lst = find_platforms_num(games_lst)
positive_ratings_lst = positive_ratings(games_lst)
average_playtime_lst = average_playtime(games_lst)
owners_lst = owners(games_lst)
names_lst = names_lst(games_lst)

build_diagrams(names_lst, platforms_num_lst, positive_ratings_lst, average_playtime_lst, owners_lst)

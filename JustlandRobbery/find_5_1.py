import json


def print_structure(struct):
    print(json.dumps(struct, indent=4, ensure_ascii=False))


def get_robberies_from_file(filename='грабители.csv'):
    """

    :return:
    [
    {
        'имя': '',
        'город': '',
        ...
    },
    {
        'имя': '',
        'город': '',
        ...
    },
    ...
    ]
    """
    with open(filename, encoding='utf-8') as file:
        robberies = []
        headers = file.readline()
        for line in file:
            clear_line = line.rstrip()  # 'Бибка, Джастленд, ультрамаркет Ультруся, ручка; помидор#10; булка, 02-11-2131, F, -'
            robbery_list = clear_line.split(', ')
            robbery_dict = {
                'имя': robbery_list[0],
                'город': robbery_list[1],
                'жертва': robbery_list[2],
                'украл': robbery_list[3],
                'дата': robbery_list[4],
                'пойман': robbery_list[5] == 'T',
                'речь': robbery_list[6]
            }
            robberies.append(robbery_dict)
        return robberies


def find_5_1_guy():
    """
    Алгоритм:
    0. Перетворити csv текст на список словників

    1. рахуємо, скільки разів кожен грабіжник був пійманий і скільки - не пійманий.
    Пакуємо це все в структуру:
    {
        'Воролеша': {'пійманий': 3, "втік": 2},
        "Аліса": {"пійманий": 0, "втік": 4},
        "Сашко": {'пійманий': 2, "втік": 0}
        ...
    }

    2. Шукаємо всіх грабіжників, які підходять під умову:
    5 разів втік, 1 раз пійманий

    3. Знайти річ, яку сказав грабіжник
    """
    thieves = {}

    robberies = get_robberies_from_file()
    for robbery in robberies:
        name = robbery['имя']
        if name not in thieves:
            thieves[name] = {'пійманий': 0, "втік": 0}

        if robbery['пойман'] is True:
            thieves[name]['пійманий'] += 1
        else:
            thieves[name]['втік'] += 1

    needed_thief_name = ''
    for thief_name in thieves:
        if thieves[thief_name]['втік'] == 5 and thieves[thief_name]['пійманий'] == 1:
            needed_thief_name = thief_name

    for robbery in robberies:
        if robbery['имя'] == needed_thief_name and robbery['пойман']:
            print(robbery['речь'])


find_5_1_guy()

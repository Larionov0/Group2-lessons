from datetime import date


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


robberies = get_robberies_from_file()

lst = []

for line in robberies:
    for el in lst:
        dict = {}
        if el['name'] != line['имя']:
            dict['name'] = line['имя']
            dict['prev date'] = line['дата']
            dict['counter'] = 0
            if line['пойман'] != False:
                dict['counter'] = 1
            lst.append(dict)
        else:
            date1 = line['дата'].split('-')
            date2 = el['prev date'].split('-')

            if (date(date1[2],date1[1],date1[0]) - date(date2[2],date2[1],date2[0])).days <= 31 and line['пойман'] == True:
                el['counter'] += 1
            else:
                el['counter'] = 1

for el in lst:
    if el['counter'] == 4:
        print(el['name'])

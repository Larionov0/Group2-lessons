import json

data = {
    'комнаты': [
        {
            'номер': 4,
            'ширина': 4.5,
            'длинна': 6.3,
            'стоимость': 4000,
            'посетителей допустимо': 3,
            'заселено': 0,
            'предметы': {'шкаф B': 2, "телевизор ACA": 1, "стол дерево": 2, "стул пластик A": 5, 'кровать C': 1}
        },
        {
            'номер': 6,
            'ширина': 5.5,
            'длинна': 2.3,
            'стоимость': 3000,
            'посетителей допустимо': 1,
            'заселено': 1,
            'предметы': {'шкаф B': 1, "стол пластик": 1, "стул пластик A": 1, 'кровать D': 1}
        },
    ]
}


def change_hotel():
    new_choise = int(input("1 - добавить комнату | 2 - удалить комнату "))
    if new_choise == 1:
        new_room = {}
        list_of_parameters = list(data['комнаты'][0].keys())
        for item in list_of_parameters:
            if item != 'предметы':
                print(item)
                new_room[item] = int(input("Введіть "))
            else:
                while True:
                    thing = input("Введіть річ(stop) ")
                    if thing == "stop":
                        break
                    new_room[thing] = int(input("Введіть кількість "))
        print(new_room)
    elif new_choise == 2:
        number_of_room = int(input("Введіть номер кімьнати "))
        for room in data['комнаты']:
            if room['номер'] == number_of_room:
                data['комнаты'].remove(room)


def find_room():
    min_square = int(input("Введіть мінімальну площу "))
    guests_number = int(input("Введіть кількість людей "))
    for room in data['комнаты']:
        if room['ширина'] * room['длинна'] >= min_square and guests_number <= (
                room['посетителей допустимо'] - room['заселено']):
            print(room["номер"], room['стоимость'])


def check_in():
    i = 0
    while i < 1:
        room_number = int(input("Введіть номер кімнати "))
        guests_number = int(input("Введіть кількість людей "))
        for room in data['комнаты']:
            if room_number == room['номер'] and guests_number <= (room['посетителей допустимо'] - room['заселено']):
                print("Вітаємо з успішним заселенням :)")
                room['заселено'] += guests_number
                i += 1
            else:
                pass
        if i < 1:
            print("Немає такої кімнати, спробуйте ще")


def statistics():
    number_of_people = 0
    number_of_people_now = 0
    square = 0
    net_worth = 0
    dict_of_things = {}

    for room in data['комнаты']:
        number_of_people += room['посетителей допустимо']
        number_of_people_now += room['заселено']
        square += room['ширина'] * room['длинна']
        net_worth += room['стоимость']
        lst_things = []
        lst_numbers = []

        lst_things = list(room['предметы'].keys())
        lst_numbers = list(room['предметы'].values())
        for i in range(len(lst_things)):
            if lst_things[i] not in dict_of_things:
                dict_of_things[lst_things[i]] = lst_numbers[i]
            else:
                dict_of_things[lst_things[i]] += lst_numbers[i]
    print(number_of_people, number_of_people_now, square, net_worth, dict_of_things)


def main(choise):
    if choise == 1:
        change_hotel()
    elif choise == 2:
        find_room()
    elif choise == 3:
        check_in()
    elif choise == 4:
        statistics()
        print("\n")


# dataToSave = json.dumps(data)
def main_menu():
    while True:
        # dataToSave = json.loads(data)
        print("--Головне меню--")
        print("1 - обустройство отеля")
        print("2 - поиск доступных номеров")
        print("3 - добавить гостей")
        print("4 - статистика")
        print("5 - выход из программы")
        choise = int(input("Ваш вибір->"))
        if choise == 5:
            break
        main(choise)
        # dataToSave = json.dumps(data)


main_menu()

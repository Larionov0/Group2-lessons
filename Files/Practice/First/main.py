FILENAME = 'Data/saving.txt'


def print_user(user):
    print(f'Користувач: {user["name"]}\n'
          f'Бали: {user["points"]}')


def main_menu(user):
    while True:
        print_user(user)
        print('1 - змінити ім`я')
        print('2 - змінити пароль')
        print('3 - клік')
        print('4 - вихід з програми')

        choice = input('Ваш вибір: ')
        if choice == '1':
            user['name'] = input('Юзернейм: ')
        elif choice == '2':
            if user['password'] != '':
                password = input('Введіть старий пароль:')
                if password != user['password']:
                    print('Пароль невірний')
                    continue

            new_password = input('Новий пароль: ')
            if 6 <= len(new_password) <= 26:
                user['password'] = new_password
            else:
                print('Поганий пароль')

        elif choice == '3':
            user['points'] += 1

        elif choice == '4':
            save(user)
            break

        else:
            pass


def save(user, filename=FILENAME):
    file = open(filename, 'wt', encoding='utf-8')
    file.write(f'{user["name"]}, {user["password"]}, {user["points"]}')
    file.close()


def load_data(filename=FILENAME):
    """
    :return: user:
    dict if exists and correct
    None in other cases
    """
    try:
        file = open(filename, 'rt', encoding='utf-8')
    except FileNotFoundError:
        return None

    try:
        str_data = file.read()
        list_data = str_data.split(', ')
        user = {
            'name': list_data[0],
            'password': list_data[1],
            'points': int(list_data[2])
        }

        file.close()
        return user
    except (IndexError, ValueError):
        print('Дані пошкоджено')
        return None


def main():
    user = load_data()
    if user is None:
        user = {
            'name': 'User',
            'password': '',
            'points': 0
        }

    if user['password'] != '':
        password = input('Пароль: ')
        if password != user['password']:
            exit()

    main_menu(user)


main()

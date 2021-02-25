from os import system


SAVINGS_FILENAME = 'Data/data.csv'


def clear():
    system('cls')


def input_string(question, min_len=0, max_len=float('inf'), is_numbers_valid=True, valid_symbols=('_', )):
    while True:
        ans = input(question)
        if len(ans) < min_len or len(ans) > max_len:
            print('Ненормальна довжина строки')
            continue
        if is_numbers_valid:
            if not ans.isalnum():
                print('Допустимі лише символи алфавіту і числа')
                continue
        else:
            if not ans.isalpha():
                print('Допустимі лише символи алфавіту')
                continue
        return ans


def print_message(message):
    print(message)
    input('\n\n<Enter>')


def is_username_exists(data, username):
    for user in data:
        if user['username'] == username:
            return True
    return False


def input_username(data):
    while True:
        username = input_string('Нікнейм: ', 4, 16)
        if is_username_exists(data, username):
            print('Такий нікнейм вжу існує!')
            continue
        return username


def save_data(data):
    with open(SAVINGS_FILENAME, 'wt', encoding='utf-8') as file:
        headers = ['username', 'password', 'coins', 'level', 'places', 'units']
        headers_str = ', '.join(headers)
        file.write(headers_str + '\n')
        for user in data:
            user_line = f"{user['username']}, {user['password']}, {user['coins']}, {user['level']}, {user['places']}, "
            for unit in user['units']:
                user_line += f"{unit}:{user['units'][unit]}; "
            user_line = user_line[:-2] + '\n'
            file.write(user_line)


def load_data():
    pass


def register_menu(data):
    username = ''
    password = ''
    while True:
        clear()
        text = '---= Реєстрація =---\n' \
               f'Нікнейм |{username}\n' \
               f'Пароль  |{password}\n' \
               f'Ваші дії:\n' \
               f'1 - нікнейм\n' \
               f'2 - пароль\n' \
               f'3 - зареэструватися\n' \
               f'4 - назад'
        print(text)
        choice = input('Ваш вибір: ')

        if choice == '1':
            username = input_username(data)
        elif choice == '2':
            password = input_string('Пароль: ', 6, 25)
        elif choice == '3':
            if username != '' and password != '':
                user = {
                    'username': username,
                    'password': password,
                    'coins': 10,
                    'level': 1,
                    'places': 1,
                    'units': {
                        'soldier': 5,
                        'turret': 1,
                        'tank': 0
                    }
                }
                data.append(user)
                save_data(data)
                print_message('Ви успішно зареєстровані!')
                return
            else:
                print('Будь ласка, заповніть всі дані!')
        else:
            return


def log_in(data, username, password):
    """
    :param data: list
    :param username:
    :param password:
    :return: dict: user if exists, else None
    """
    for user in data:
        if user['username'] == username and user['password'] == password:
            return user
    return None


def log_in_menu(data):
    username = ''
    password = ''
    while True:
        clear()
        text = '---= Авторизація =---\n' \
               f'Нікнейм |{username}\n' \
               f'Пароль  |{password}\n' \
               f'Ваші дії:\n' \
               f'1 - нікнейм\n' \
               f'2 - пароль\n' \
               f'3 - увійти\n' \
               f'4 - назад'
        print(text)
        choice = input('Ваш вибір: ')

        if choice == '1':
            username = input_string('Нікнейм: ', 4, 16)
        elif choice == '2':
            password = input_string('Пароль: ', 6, 25)
        elif choice == '3':
            if username != '' and password != '':
                user = log_in(data, username, password)
                if user:
                    return game_main_menu(data, user)
                else:
                    print_message('Такого юзера не існує')
            else:
                print_message('Будь ласка, заповніть всі дані!')

        elif choice == '4':
            return


def game_main_menu(data, user):
    while True:
        save_data(data)
        clear()
        text = '---= Ваша база =---\n' \
               f'Користувач {user["username"]}\n' \
               f'Монет: {user["coins"]}\n' \
               f'Level: {user["level"]}\n'
        text += 'Units:\n'
        for unit in user['units']:
            text += f'{unit}: {user["units"][unit]}\n'

        text += '1 - атакувати гравця\n' \
                '2 - чекати хвилю\n' \
                '3 - вийти з аккаунту'
        print(text)
        choice = input('Ваш вибір: ')
        if choice == '3':
            return


def main_menu(data):
    while True:
        save_data(data)
        clear()
        text = '---= Головне меню =---\n' \
               '1 - зареєструватися\n' \
               '2 - увійти\n' \
               '3 - віийти з програми'
        print(text)
        choice = input('Ваш вибір: ')
        if choice == '1':
            register_menu(data)
        elif choice == '2':
            log_in_menu(data)
        elif choice == '3':
            break
        else:
            pass


def main():
    # data = [
    #     {
    #         'username': 'username',
    #         'password': 'password',
    #         'coins': 10,
    #         'level': 2,
    #         'places': 2,
    #         'units': {
    #             'soldier': 10,
    #             'turret': 4,
    #             'tank': 2
    #         }
    #     },
    #     {
    #         'username': 'username2',
    #         'password': 'password2',
    #         'coins': 124,
    #         'level': 5,
    #         'places': 4,
    #         'units': {
    #             'soldier': 1000,
    #             'turret': 1,
    #             'tank': 6
    #         }
    #     },
    # ]
    data = load_data()
    main_menu(data)


main()

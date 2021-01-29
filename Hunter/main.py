from os import system
import random
import time
import msvcrt

CEND = '\33[0m'
CBOLD = '\33[1m'
CITALIC = '\33[3m'
CURL = '\33[4m'
CBLINK = '\33[5m'
CBLINK2 = '\33[6m'
CSELECTED = '\33[7m'

CBLACK = '\33[30m'
CRED = '\33[31m'
CGREEN = '\33[32m'
CYELLOW = '\33[33m'
CBLUE = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE = '\33[36m'
CWHITE = '\33[37m'

CBLACKBG = '\33[40m'
CREDBG = '\33[41m'
CGREENBG = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG = '\33[46m'
CWHITEBG = '\33[47m'

CGREY = '\33[90m'
CRED2 = '\33[91m'
CGREEN2 = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2 = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2 = '\33[96m'
CWHITE2 = '\33[97m'

CGREYBG = '\33[100m'
CREDBG2 = '\33[101m'
CGREENBG2 = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2 = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2 = '\33[106m'
CWHITEBG2 = '\33[107m'


def clear():
    system('cls')


def press(text=''):
    print(text)
    return msvcrt.getch().decode()


def input_int(text, error_message='Це не число! Спробуйте ще раз.', min_value=None, max_value=None):
    while True:
        number_str = input(text)  # '213d'
        if number_str.isdigit():
            number = int(number_str)
            if min_value is not None:
                if number < min_value:
                    print('Замале число!')
                    continue

            if max_value is not None:
                if number > max_value:
                    print('Завелике число!')
                    continue

            return number
        else:
            print(error_message)


def create_matrix(n, m, value='-'):
    matrix = []
    for _ in range(n):
        row = [value for _ in range(m)]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:  # row=[4, '1', 6, 2, 5]
        row_text = '|'
        for el in row:
            row_text += str(el) + ' '
        row_text = row_text[:-1] + '|'
        print(row_text)


def calculate_distance(point1, point2):
    """
    :param point1: list[int]
    :param point2: list[int]
    :return: int   - distance

    >> calculate_distance([1, 2], [4, 2])
    3
    >> calculate_distance([1, 1], [4, 5])
    5.0
    >> calculate_distance([1, 1], [2, 2])
    1.4142135623730951
    """
    a = point2[0] - point1[0]
    b = point2[1] - point1[1]
    c = (a ** 2 + b ** 2) ** (1 / 2)
    return c


def draw_creature(matrix, creature):
    """
    Функція для того, щоб намалювати створіння на матриці.
    :param matrix: list[list]  - поле
    :param creature: dict    {face, coords}
    :return:
    """
    matrix[creature['coords'][0]][creature['coords'][1]] = creature['face']
    # if 'face' in creature:
    #     matrix[creature['coords'][0]][creature['coords'][1]] = creature['face']
    # else:
    #     matrix[creature['coords'][0]][creature['coords'][1]] = animals_prototypes[creature['type']]['face']


def draw_creatures(matrix, creatures):
    for creature in creatures:
        draw_creature(matrix, creature)


def hero_makes_move(hero, matrix, animals):
    clear()
    print_matrix(matrix)
    print("--= Головне меню =--")
    print("Ваші деталі: ", hero['details'])
    print("Ваші дії:")
    print("WASD - рухатись")
    print('x - зробити вистріл')
    choice = press()
    if choice in ['w', 'a', 's', 'd']:
        creatures_moves(hero, choice)
    elif choice == 'x':
        hero_shoots(hero, animals, matrix)


def hero_shoots(hero, animals, matrix):
    type_ = hero['main_weapon']['type']
    if type_ == 'bow':
        bow_shot(hero, animals)
    elif type_ == 'slingshot':
        slingshot_shot(hero, animals)


def slingshot_shot(hero, animals):
    matrix = create_matrix(N, M)
    draw_creatures(matrix, animals)

    i = 0
    while i < N:
        j = 0
        while j < M:
            if calculate_distance([i, j], hero['coords']) <= hero['main_weapon']['range']:
                matrix[i][j] = '+'
            j += 1
        i += 1

    draw_creature(matrix, hero)

    animals_on_target = []
    for animal in animals:
        if calculate_distance(animal['coords'], hero['coords']) <= hero['main_weapon']['range']:
            animals_on_target.append(animal)
            matrix[animal['coords'][0]][animal['coords'][1]] = CRED + animal['targeted_face'] + CEND

    clear()
    print_matrix(matrix)

    print('Виберіть тварину:')
    print('0 - назад')
    number = 1
    for animal in animals_on_target:
        print(f"{number} - {animal['type']} {animal['name']} ({animal['hp']} hp)  {animal['coords']}")
        number += 1

    choice = input_int('Ваш вибір: ', min_value=0, max_value=len(animals_on_target))
    if choice == 0:
        return
    animal = animals_on_target[choice - 1]
    animal_loose_hp(animal, hero['main_weapon']['damage'], animals, hero)


def bow_shot(hero, animals):
    direction = press('Виберіть напрям: ')
    arrow = {
        'type': 'arrow',
        'damage': hero['main_weapon']['damage'],
        'direction': direction,
        'energy': hero['main_weapon']['range'],
        'coords': hero['coords'].copy(),
        'face': 'x'
    }
    arrow_fly(arrow, hero, animals)


def arrow_fly(arrow, hero, animals):
    while arrow['energy'] >= 0:
        clear()
        matrix = create_matrix(N, M)
        draw_creature(matrix, hero)
        draw_creatures(matrix, animals)
        draw_creature(matrix, arrow)
        print_matrix(matrix)
        time.sleep(0.3)

        for animal in animals:
            if animal['coords'] == arrow['coords']:
                animal_loose_hp(animal, arrow['damage'], animals, hero)
                return

        creatures_moves(arrow, arrow['direction'])
        arrow['energy'] -= 1


def animal_loose_hp(animal, damage, animals, hero):
    animal['hp'] -= damage
    if animal['hp'] <= 0:
        animals.remove(animal)
        hero['details'] += animal['details']


def creatures_moves(creature, direction):
    if direction == 'w':
        if creature['coords'][0] != 0:
            creature['coords'][0] -= 1
    elif direction == 'a':
        if creature['coords'][1] == 0:
            creature['coords'][1] = M - 1
        else:
            creature['coords'][1] -= 1
    elif direction == 's':
        if creature['coords'][0] != N - 1:
            creature['coords'][0] += 1
    elif direction == 'd':
        if creature['coords'][1] == M - 1:
            creature['coords'][1] = 0
        else:
            creature['coords'][1] += 1


def is_kurka_catched(animals, hero):
    catched_animals = []
    for animal in animals:
        if animal['coords'] == hero['coords']:
            catched_animals.append(animal)
            hero['details'] += animal['details']

    for animal in catched_animals:
        animals.remove(animal)


def animals_makes_move(animals):
    for animal in animals:
        animal_makes_move(animal)


def animal_makes_move(animal):
    if animal['type'] == 'kurka':
        kurka_makes_move(animal)
    elif animal['type'] == 'deer':
        pass
    elif animal['type'] == 'rabbit':
        rabbit_makes_move(animal, hero)


def rabbit_makes_move(rabbit, hero):
    if calculate_distance(rabbit['coords'], hero['coords']) > 3:
        direction = random.choice(['w', 'a', 's', 'd'])
        creatures_moves(rabbit, direction)
    else:
        rabbit_run(rabbit, hero)


def rabbit_run(rabbit, hero):
    y1 = hero['coords'][0]
    x1 = hero['coords'][1]
    y2 = rabbit['coords'][0]
    x2 = rabbit['coords'][1]

    direction = False
    # directly
    if y1 == y2 and x1 < x2:
        direction = 'd'
    elif y1 == y2 and x1 > x2:
        direction = 'a'
    elif y1 > y2 and x1 == x2:
        direction = 'w'
    elif y1 < y2 and x1 == x2:
        direction = 's'

        # obliquely
    elif y1 > y2 and x1 > x2:
        direction = random.choice(['a', 'w'])
    elif y1 > y2 and x1 < x2:
        direction = random.choice(['d', 'w'])
    elif y1 < y2 and x1 > x2:
        direction = random.choice(['a', 's'])
    elif y1 < y2 and x1 < x2:
        direction = random.choice(['d', 's'])

    creatures_moves(rabbit, direction)


def kurka_makes_move(kurka):
    direction = random.choice(['w', 'a', 's', 'd'])
    creatures_moves(kurka, direction)


def check_spawn_animals(round_, animals):
    if round_ % 20 == 0:
        spawn_kurka(animals)
    elif round_ % 40 == 0:
        pass


def spawn_kurka(animals):
    kurka = {
        'type': 'kurka',
        'name': random.choice(['New', 'Biba', 'Vasya', 'Petya', 'Marina']),
        'hp': 3,
        'face': 'k',
        'targeted_face': 'K',
        'coords': [random.randint(0, N - 1), random.randint(0, M - 1)],
        'details': 3
    }
    animals.append(kurka)


def main(animals, hero):
    round_ = 1
    while True:
        matrix = create_matrix(N, M)
        draw_creature(matrix, hero)
        draw_creatures(matrix, animals)

        hero_makes_move(hero, matrix, animals)
        is_kurka_catched(animals, hero)
        animals_makes_move(animals)
        is_kurka_catched(animals, hero)
        check_spawn_animals(round_, animals)
        round_ += 1


N = 14
M = 18

weapons = [
    {
        'type': 'bow',
        'name': 'Base bow',
        'damage': 3,
        'range': 4
    },
    {
        'type': 'slingshot',
        'name': 'Base slingshot',
        'damage': 2,
        'range': 4
    }
]

hero = {
    'name': 'Bob',
    'hp': 20,
    'face': f'{CBLUE}@{CEND}',
    'max_hp': 20,
    'coords': [1, 2],
    'details': 0,
    'main_weapon': {
        'type': 'bow',
        'name': 'Base bow',
        'damage': 3,
        'range': 4
    }
}

animals_prototypes = {
    'kurka': {
        'max_hp': 3,
        'face': 'k',
        'targeted_face': 'K',
        'details': 3
    },
    'duck': {
        'max_hp': 2,
        'face': 'd',
        'targeted_face': 'D',
        'details': 4
    }
}

animals = [
    {
        'type': 'kurka',
        'name': 'Ryaba',
        'hp': 3,
        'face': 'k',
        'targeted_face': 'K',
        'coords': [5, 5],
        'details': 3
    },
    {
        'type': 'kurka',
        'name': 'Boba',
        'hp': 3,
        'face': 'k',
        'targeted_face': 'K',
        'coords': [5, 6],
        'details': 3
    },
    {
        'type': 'kurka',
        'name': 'Marusya',
        'hp': 3,
        'face': 'k',
        'targeted_face': 'K',
        'coords': [6, 5],
        'details': 3
    },
    {
        'type': 'rabbit',
        'name': 'Biba',
        'hp': 2,
        'face': 'r',
        'targeted_face': 'R',
        'coords': [5, 7],
        'details': 5
    }
]

main(animals, hero)

name = 'Bob'
age = 12
hobbies = 4

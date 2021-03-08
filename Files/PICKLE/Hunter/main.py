from os import system
import random
import msvcrt
import time
import pickle

n = 18
m = 18

SAVINGS_FILENAME = 'savings.dat'

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


def press():
    inp = msvcrt.getch().decode()
    return inp


def print_line(n=40):
    print('-' * n)


def print_message(text):
    print(f"{CGREEN}{text}{CEND}")
    input('\n\n<Enter>')


def input_int(text, min_=None, max_=None):
    while True:
        number_str = input(text)
        if number_str.isdigit():
            number = int(number_str)
            normal = True
            if min_:
                if number < min_:
                    print('Замале число')
                    normal = False
            if max_:
                if number > max_:
                    print('Завелике число')
                    normal = False

            if normal is True:
                return number
        else:
            print('Це не число. Спробуйте ще!')


def distance(coords1, coords2):
    a = coords1[0] - coords2[0]
    b = coords1[1] - coords2[1]
    c = (a ** 2 + b ** 2) ** 0.5
    return c


def create_matrix(n, m, element='-'):
    matrix = []
    i = 0
    while i < n:
        row = []
        j = 0
        while j < m:
            row.append(element)
            j += 1
        matrix.append(row)
        i += 1
    return matrix


def print_matrix(matrix):
    for row in matrix:  # [4, 2, 5, 4]
        text = '|'
        for el in row:
            text += str(el) + " "
        text = text[:-1] + "|"
        print(text)


def draw_creature(creature, pole):
    pole[creature['coords'][0]][creature['coords'][1]] = creature['face']


def draw_animals(animals, pole):
    for animal in animals:
        draw_creature(animal, pole)


def creature_moves(creature, direction):
    """
    :param creature:
    :param direction: str: WASD
    """
    if direction == 'W':
        if creature['coords'][0] != 0:
            creature['coords'][0] -= 1
    elif direction == 'A':
        if creature['coords'][1] != 0:
            creature['coords'][1] -= 1
    elif direction == 'S':
        if creature['coords'][0] != n - 1:
            creature['coords'][0] += 1
    elif direction == 'D':
        if creature['coords'][1] != m - 1:
            creature['coords'][1] += 1


def print_hero(hero):
    print(f"Здоров'я: {hero['hp']}/{hero['max_hp']}. Деталі: {hero['details']}")
    print(f"Стріли: {hero['inventory']['ammo']['arrows']}")
    print(f"Каміння: {hero['inventory']['ammo']['rocks']}")


def hero_makes_move(data, pole, store, trader):
    hero, animals, things = data['hero'], data['animals'], data['things']
    is_store_available = False
    if trader['visible'] and trader['coords'] == hero['coords']:
        is_store_available = True

    print_matrix(pole)
    print("--= Головне меню =--")
    print_hero(hero)
    print('e - стріляти')
    print('i - інвентар')
    if is_store_available:
        print('m - торгувати')
    print("WASD: ")
    choice = press()
    if choice.lower() in ['w', 'a', 's', 'd']:
        creature_moves(hero, choice.upper())
        check_if_hero_stepped_in_thing(hero, things)
    elif choice == 'e':
        shot(hero, pole, animals, things)
    elif choice == 'i':
        inventory_menu(hero)
    elif is_store_available and choice == 'm':
        store_menu(store, hero, trader)


def check_if_hero_stepped_in_thing(hero, things):
    for thing in things:
        if thing['coords'] == hero['coords']:
            hero_stepped_on_thing(hero, thing, things)


def hero_stepped_on_thing(hero, thing, things):
    if thing['type'] == 'details':
        hero['details'] += thing['count']
        things.remove(thing)


def inventory_menu(hero):
    while True:
        clear()
        print('----= Інвентар =----')
        print('0 - назад\n'
              '1 - weapons\n'
              '2 - ammo')
        choice = input_int('Ваш вибір: ')
        if choice == 1:
            weapons_inventory_menu(hero)
        elif choice == 2:
            clear()
            print('---= Боєприпаси =---')
            print(hero['inventory']['ammo'])
        elif choice == 0:
            break


def weapons_inventory_menu(hero):
    while True:
        clear()
        print('---= Зброя =---')
        print('0 - назад')
        number = 1
        for weapon in hero['inventory']['weapons']:
            print(f"{number} - {CGREEN}{weapon['type']}{CEND} '{weapon['name']}'")
            number += 1
        choice = input_int('Ваш вибір: ')
        if choice == 0:
            return
        if choice < 1 or choice > len(hero['inventory']['weapons']):
            print('Не то пальто')
        else:
            index = choice - 1
            weapon = hero['inventory']['weapons'][index]
            weapon_menu(hero, weapon)


def print_weapon(weapon, price=False):
    if weapon['type'] in ['bow', 'slingshot']:
        print_line()
        print(f"{CGREEN}{weapon['type']}{CEND} '{weapon['name']}'\n"
              f"damage: {weapon['damage']}\n"
              f"range: {weapon['range']}")
        if price is True:
            print(f"{weapon['price']} $")
        print_line()


def weapon_menu(hero, weapon):
    while True:
        clear()
        print('---= Меню зброї =---')
        print_hero(hero)
        print_weapon(weapon)
        print('0 - назад\n'
              '1 - встановити як основну\n'
              '2 - розібрати на деталі')
        choice = input('Ваш вибір:')
        if choice == '1':
            hero['main_weapon'] = weapon
            input(f'{CGREEN}Зброя успішно встановлена як основна!{CEND}')
        elif choice == '2':
            pass
        elif choice == '0':
            return


def store_menu(store, hero, trader):
    clear()
    print(f'------= Магазин {trader["name"]} =-------')
    print_hero(hero)
    print(f'0 - назад\n'
          f'1 - зброя\n'
          f'2 - боєприпаси\n'
          f'3 - їжа')
    choice = input('Ваш вибір: ')
    if choice == '1':
        weapons_store_menu(hero, store, trader)
    elif choice == '2':
        ammo_store_menu(hero, store, trader)
    elif choice == '3':
        pass
    elif choice == '0':
        return


def ammo_store_menu(hero, store, trader):
    while True:
        clear()
        print('---= Зброя торговця =---')
        print_hero(hero)
        print('0 - назад')
        number = 1
        for ammo_dict in store['ammo']:  # ammo_dict={'type': 'rocks', 'count': 20, 'price': 8}
            print(f"{number} - {ammo_dict['type']} X{ammo_dict['count']} ({ammo_dict['price']} $)")
            number += 1
        number = input_int('Ваш вибір: ', min_=0, max_=len(store['ammo']))
        if number == 0:
            return
        index = number - 1
        ammo_dict = store['ammo'][index]
        if hero['details'] >= ammo_dict['price']:
            hero['inventory']['ammo'][ammo_dict['type']] += ammo_dict['count']
            hero['details'] -= ammo_dict['price']


def weapons_store_menu(hero, store, trader):
    while True:
        clear()
        print('---= Зброя торговця =---')
        print_hero(hero)
        print('0 - назад')
        number = 1
        for weapon in store['weapons']:
            print(f"{number} - {CGREEN}{weapon['type']}{CEND} '{weapon['name']}' ({weapon['price']} $)")
            number += 1
        choice = input_int('Ваш вибір: ')
        if choice == 0:
            return
        if choice < 1 or choice > len(store['weapons']):
            print('Не то пальто')
        else:
            index = choice - 1
            weapon = store['weapons'][index]
            store_weapon_menu(hero, weapon)


def store_weapon_menu(hero, weapon):
    while True:
        clear()
        print('---= Меню зброї в магазині =---')
        print_hero(hero)
        print_weapon(weapon, price=True)
        print('0 - назад\n'
              '1 - купити')
        choice = input('Ваш вибір:')
        if choice == '1':
            if hero['details'] >= weapon['price']:
                hero['details'] -= weapon['price']
                hero['inventory']['weapons'].append(weapon)
                print_message('Зброя куплена!')
            else:
                print_message('Не вистачає грошей:(')
        elif choice == '0':
            return


def shot(hero, pole, animals, things):
    if hero['main_weapon'] is None:
        print_message('У вас немає зброї!')
        return

    if hero['main_weapon']['type'] == 'bow':
        bow_shot(hero, pole, animals, things)
    elif hero['main_weapon']['type'] == 'slingshot':
        slinghot_shot(hero, pole, animals, things)


def slinghot_shot(hero, pole, animals, things):
    if hero['inventory']['ammo']['rocks'] == 0:
        print_message('У вас не вистачає каміння!')
        return

    targeted_animals = []

    i = 0
    while i < len(pole):
        j = 0
        while j < len(pole[i]):
            if distance([i, j], hero['coords']) <= hero['main_weapon']['range']:
                pole[i][j] = 'x'
                for animal in animals:
                    if animal['coords'] == [i, j]:
                        targeted_animals.append(animal)
                        pole[i][j] = CRED + animal['targeted_face'] + CEND
            j += 1
        i += 1
    draw_creature(hero, pole)

    clear()
    print_matrix(pole)
    choose_animal_for_sling_shot(targeted_animals, hero, animals, things)


def choose_animal_for_sling_shot(targeted_animals, hero, animals, things):
    print('---= Виберіть тварину =---')
    print('0 - назад')
    i = 1
    for animal in targeted_animals:
        print(f"{i} - {animal['type']} {animal['name']} ({animal['hp']} hp) ({animal['coords']})")
        i += 1

    while True:
        number = input_int('Ваш вибір: ')
        if number == 0:
            return
        index = number - 1

        if 0 <= index < len(targeted_animals):
            animal = targeted_animals[index]
            animal_loose_hp(animal, hero['main_weapon']['damage'], animals, things)
            hero['inventory']['ammo']['rocks'] -= 1
            break
        else:
            print_message('Такого варіанту не було')


def bow_shot(hero, pole, animals, things):
    if hero['inventory']['ammo']['arrows'] == 0:
        print_message('У вас не вистачає стріл!')
        return

    print('Виберіть напрям (WASD): ')
    direction = press()
    bow_shot_with_direction(hero, direction, pole, animals, things)


def bow_shot_with_direction(hero, direction, pole, animals, things):
    hero['inventory']['ammo']['arrows'] -= 1

    arrow = {
        'face': 'x',
        'coords': hero['coords'].copy(),
        'energy': hero['main_weapon']['range'],
        'damage': hero['main_weapon']['damage'],
        'direction': direction.upper()
    }
    arrow_fly(arrow, pole, animals, hero, things)


def arrow_fly(arrow, pole, animals, hero, things):
    while arrow['energy'] >= 0:
        pole = create_matrix(n, m)
        draw_creature(hero, pole)
        draw_animals(animals, pole)
        pole[arrow['coords'][0]][arrow['coords'][1]] = arrow['face']
        clear()
        print_matrix(pole)

        result = False
        for animal in animals:
            if animal['coords'] == arrow['coords']:
                result = True
                break
        if result is True:
            animal_loose_hp(animal, arrow['damage'], animals, things)
            break

        creature_moves(arrow, arrow['direction'])
        arrow['energy'] -= 1
        time.sleep(0.5)


def animal_loose_hp(animal, damage, animals, things):
    animal['hp'] -= damage
    if animal['hp'] <= 0:
        die(animal, animals, things)


def die(animal, animals, things):
    animals.remove(animal)
    drop_things(animal, things)


def drop_things(animal, things):
    if animal['type'] == 'курка':
        things.append({
            'type': 'details',
            'coords': animal['coords'].copy(),
            'count': 3,
            'face': '#'
        })
    elif animal['type'] == 'заєць':
        things.append({
            'type': 'details',
            'coords': animal['coords'].copy(),
            'count': 4,
            'face': '#'
        })


def animals_makes_move(animals, hero, things):
    for animal in animals:
        animal_makes_move(animal, animals, hero, things)


def animal_makes_move(animal, animals, hero, things):
    if animal['type'] == 'курка':
        kurka_makes_move(animal, animals, hero)
    elif animal['type'] == 'олень':
        pass
    elif animal['type'] == 'заєць':
        zayac_makes_move(animal, animals, hero)
    elif animal['type'] == 'вовк':
        vovk_makes_move(animal, animals, hero, things)
    else:
        pass


def get_creatures_in_radius(creature, radius, animals, hero):
    creatures_in_radius = []
    for animal in animals:
        if distance(creature['coords'], animal['coords']) < radius:
            creatures_in_radius.append(animal)
    if distance(creature['coords'], hero['coords']) < radius:
        creatures_in_radius.append(hero)
    return creatures_in_radius


def vovk_makes_move(wolf, animals, hero, things):
    if wolf['cooldown'] > 0:
        wolf['cooldown'] -= 1
        if wolf['cooldown'] == 0:
            wolf['energy'] = wolf['max_energy']
        return

    if wolf['target'] is None:
        creatures_in_radius = get_creatures_in_radius(wolf, wolf['radius'], animals, hero)
        prey_in_radius = [creature for creature in creatures_in_radius if creature['type'] in prey_types]
        min_distance = float('inf')
        closest_prey = None
        for prey in prey_in_radius:
            d = distance(wolf['coords'], prey['coords'])
            if d < min_distance:
                min_distance = d
                closest_prey = prey

        wolf['target'] = closest_prey

    if wolf['target'] is None:
        wolf['energy'] += 1
        if wolf['energy'] > wolf['max_energy']:
            wolf['energy'] = wolf['max_energy']
        return

    target = wolf['target']

    check_if_predator_eats_details(wolf, things)

    check_if_predator_catch_prey(wolf, animals + [hero], things, animals)
    if wolf['coords'][0] > target['coords'][0]:
        creature_moves(wolf, 'W')
    elif wolf['coords'][0] < target['coords'][0]:
        creature_moves(wolf, 'S')
    else:
        if wolf['coords'][1] > target['coords'][1]:
            creature_moves(wolf, 'A')
        elif wolf['coords'][1] < target['coords'][1]:
            creature_moves(wolf, 'D')
    result = check_if_predator_catch_prey(wolf, animals + [hero], things, animals)

    wolf['energy'] -= 1
    if wolf['energy'] <= 0:
        wolf['cooldown'] = 5
        wolf['target'] = None
    if result:
        wolf['cooldown'] = 3


def check_if_predator_catch_prey(predator, creatures, things, animals):
    for animal in creatures:
        if animal['type'] in prey_types:
            if animal['coords'] == predator['coords']:
                animal_loose_hp(animal, predator['attack'], animals, things)
                return True


def check_if_predator_eats_details(predator, things):
    for thing in things:
        if thing['type'] == 'details':
            if predator['coords'] == thing['coords']:
                if random.randint(1, 100) <= predator['chance_for_detail_eating']:
                    decrease_details_count(thing, things)
                    return


def decrease_details_count(details, things):
    details['count'] -= random.randint(1, 2)
    if details['count'] <= 0:
        things.remove(details)


def zayac_makes_move(zayac, animals, hero):
    if distance(zayac['coords'], hero['coords']) <= zayac['radius']:
        if zayac['coords'][0] > hero['coords'][0]:
            creature_moves(zayac, 'S')
        elif zayac['coords'][0] < hero['coords'][0]:
            creature_moves(zayac, 'W')
        else:
            if zayac['coords'][1] > hero['coords'][1]:
                creature_moves(zayac, 'D')
            else:
                creature_moves(zayac, 'A')
    else:
        direction = random.choice(['W', 'A', 'S', 'D'])
        creature_moves(zayac, direction)


def kurka_makes_move(kurka, animals, hero):
    direction = random.choice(['W', 'A', 'S', 'D'])
    creature_moves(kurka, direction)


def is_kurka_catched(animals, hero):
    dead_kurki = []
    for animal in animals:
        if animal['type'] == 'курка':
            if animal['coords'] == hero['coords']:
                hero['details'] += 3
                dead_kurki.append(animal)
    for kurka in dead_kurki:
        animals.remove(kurka)


def spawn_animals(animals, hod):
    if hod % 20 == 0:
        spawn_kurka(animals)
    if hod % 50 == 0:
        spawn_olen(animals)
    if hod % 30 == 0:
        spawn_zayac(animals)


def spawn_zayac(animals):
    zayac = {
        'type': 'заєць',
        'name': random.choice(['Алекс', "Дуб", "Катрина", "Олекса"]),
        'face': 'z',
        'targeted_face': 'Z',
        'hp': 2,
        'coords': [random.randint(0, n - 1), random.randint(0, m - 1)],
        'radius': 4 if random.randint(1, 100) <= 90 else 6  # деякі зайці далеко бачать
    }
    animals.append(zayac)


def spawn_kurka(animals):
    kurka = {
        'type': 'курка',
        'name': random.choice(['Ryaba', 'Masha', 'Olya', 'Kyrylo', 'Katia']),
        'face': 'k',
        'targeted_face': '₭',
        'hp': 3,
        'coords': [random.randint(0, n - 1), random.randint(0, m - 1)]
    }
    animals.append(kurka)


def spawn_olen(animals):
    pass


def trader_move(trader):
    trader['life_cycle'] += 1
    if trader['life_cycle'] == 40:
        trader['visible'] = True
        trader['coords'] = random.choice([[0, 0], [0, m - 1], [n - 1, 0], [n - 1, m - 1]])
    elif trader['life_cycle'] == 70:
        trader['visible'] = False
        trader['life_cycle'] = 0


def draw_trader(trader, pole):
    if trader['visible']:
        draw_creature(trader, pole)


def draw_things(things, pole):
    for thing in things:
        draw_creature(thing, pole)


def save_data(data):
    with open(SAVINGS_FILENAME, 'wb') as file:
        file.write(pickle.dumps(data))


def load_data():
    with open(SAVINGS_FILENAME, 'rb') as file:
        data = pickle.loads(file.read())
    return data


def try_to_load_data():
    try:
        return load_data()
    except Exception as ex:
        print('Сталася помилка з файлом збереження:')
        print(ex)
        print('Створюємо нові дані')
        input('<Enter>')
        return create_init_data()


def create_init_data():
    hero = {
        'type': 'мисливець',
        'face': CGREEN + CBOLD + '+' + CEND,
        'hp': 100,
        'max_hp': 100,
        'coords': [1, 1],
        'details': 0,
        'main_weapon': None,
        'inventory': {
            'weapons': [],
            'ammo': {
                'arrows': 10,
                'rocks': 10
            }
        }
    }

    animals = [
        {
            'type': 'курка',
            'name': 'Ryaba',
            'face': 'k',
            'targeted_face': '₭',
            'hp': 3,
            'coords': [5, 5]
        },
        {
            'type': 'курка',
            'name': 'Boba',
            'face': 'k',
            'targeted_face': '₭',
            'hp': 3,
            'coords': [6, 5]
        },
        {
            'type': 'курка',
            'name': 'Marusya',
            'face': 'k',
            'targeted_face': '₭',
            'hp': 3,
            'coords': [5, 6],
        },
        {
            'type': 'заєць',
            'name': 'Пень',
            'face': 'z',
            'targeted_face': 'Z',
            'hp': 2,
            'coords': [7, 6],
            'radius': 4
        },
        {
            'type': 'вовк',
            'name': 'Вова',
            'face': 'w',
            'targeted_face': 'W',
            'hp': 5,
            'coords': [10, 10],
            'chance_for_detail_eating': 40,
            'radius': 3,
            'attack': 3,
            'target': None,
            'energy': 10,
            'max_energy': 10,
            'cooldown': 0
        }
    ]

    things = [
        {
            'type': 'details',
            'count': 2,
            'coords': [9, 9],
            'face': '#'
        }
    ]

    trader = {
        'name': 'Bob',
        'coords': [],
        'face': f'{CBOLD}{CYELLOW}${CEND}',
        'visible': False,
        'life_cycle': 0
    }

    data = {
        'hero': hero,
        'animals': animals,
        'things': things,
        'trader': trader
    }
    return data


def main():
    data = try_to_load_data()
    things, animals, hero, trader = data['things'], data['animals'], data['hero'], data['trader']
    hod = 1
    while True:
        save_data(data)
        clear()
        pole = create_matrix(n, m)
        draw_things(things, pole)
        draw_creature(hero, pole)
        draw_animals(animals, pole)
        draw_trader(trader, pole)

        hero_makes_move(data, pole, store, trader)
        is_kurka_catched(animals, hero)
        animals_makes_move(animals, hero, things)
        is_kurka_catched(animals, hero)

        spawn_animals(animals, hod)
        trader_move(trader)
        hod += 1


prey_types = ['курка', 'заєць', 'мисливець']
predator_types = ['мисливець', "вовк"]
store = {
    'weapons': [
        {
            'type': 'bow',
            'name': 'Base bow',
            'damage': 3,
            'range': 4,
            'price': 15
        },
        {
            'type': 'slingshot',
            'name': 'Base slingshot',
            'damage': 2,
            'range': 3,
            'price': 15
        },
        {
            'type': 'bow',
            'name': 'Мисливський лук',
            'damage': 5,
            'range': 4,
            'price': 40
        },
        {
            'type': 'slingshot',
            'name': 'Big slingshot',
            'damage': 2,
            'range': 5,
            'price': 35
        },
    ],
    'ammo': [
        {
            'type': 'rocks',
            'count': 20,
            'price': 8
        },
        {
            'type': 'arrows',
            'count': 15,
            'price': 10
        },
        {
            'type': 'rocks',
            'count': 60,
            'price': 20
        },
    ]
}


main()

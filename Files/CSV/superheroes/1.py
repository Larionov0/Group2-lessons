from json import dumps


FILENAME = 'superheroes.csv'


def get_superheroes_list_from_file(filename=FILENAME):
    """
    :param filename:
    :return: list[dict]
    """
    superheroes = []

    with open(filename, 'rt', encoding='utf-8') as file:
        headers = file.readline()
        for line in file:
            clear_line = line.rstrip()  # 1, Боб, 26, пістоль; мішок, 298, 56
            line_list = clear_line.split(', ')  # ['1', 'Боб', '26', 'пістоль; мішок', '298', '56']
            superhero = {
                'id': int(line_list[0]),
                'name': line_list[1],
                'age': int(line_list[2]),
                'items': line_list[3].split('; '),
                'criminals_count': int(line_list[4]),
                'power': int(line_list[5])
            }
            superheroes.append(superhero)
    return superheroes


def find_most_effective_superhero(superheroes):
    """
    :param superheroes:
    :return: list[dict] - супергерої, які піймали найбільше злочинців
    """
    max_count = 0
    effective_heroes = []
    for hero_dict in superheroes:
        if hero_dict['criminals_count'] > max_count:
            max_count = hero_dict['criminals_count']
            effective_heroes.clear()
            effective_heroes.append(hero_dict)
        elif hero_dict['criminals_count'] == max_count:
            effective_heroes.append(hero_dict)
    return effective_heroes


def main():
    superheroes = get_superheroes_list_from_file()
    most_effective = find_most_effective_superhero(superheroes)

    print(dumps(most_effective, indent=4, ensure_ascii=False))
    #  print(dumps(superheroes, indent=4, ensure_ascii=False))


main()

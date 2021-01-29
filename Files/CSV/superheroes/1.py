from json import dumps


FILENAME = 'superheroes.csv'


def get_superheroes_list_from_file(filename=FILENAME):
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


superheroes = get_superheroes_list_from_file()
print(dumps(superheroes, indent=4, ensure_ascii=False))

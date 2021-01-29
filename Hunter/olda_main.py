from os import system
import random

n = 14
m = 18

hero_name = 'Hunter'
hero_hp = hero_max = 20
hero_coords = [1, 2]
hero_details = 0
hero_face = '@'

animals = [
    ['kurka', 'Ryaba', 3, 'k', [5, 6], 3],
    ['kurka', 'Boba', 3, 'k', [4, 5], 3],
    ['kurka', 'Marusya', 3, 'k', [5, 5], 3]
    ]

while True:
    # створення матриці
    matrix = []
    i = 0
    while i < n:
        row = ['-'] * m
        matrix.append(row)
        i += 1

    # викладаємо героя на матрицю
    matrix[hero_coords[0]][hero_coords[1]] = hero_face
    # викладаємо тварин на матрицю
    for animal in animals:
        matrix[animal[4][0]][animal[4][1]] = animal[3]
    
    # виводимо матрицю на екран
    system('cls')  # очистка екрану
    for row in matrix:  # row=[4, '1', 6, 2, 5]
        row_text = '|'
        for el in row:
            row_text += str(el) + ' '
        row_text = row_text[:-1] + '|'
        print(row_text)

    # хід героя
    print("--= Головне меню =--")
    print("Ваші деталі: ", hero_details)
    print("Ваші дії:")
    print("WASD")
    choice = input()
    if choice == 'w':
        if hero_coords[0] != 0:
            hero_coords[0] -= 1
    elif choice == 'a':
        if hero_coords[1] == 0:
            hero_coords[1] = m - 1
        else:
            hero_coords[1] -= 1
    elif choice == 's':
        if hero_coords[0] != n - 1:
            hero_coords[0] += 1
    elif choice == 'd':
        if hero_coords[1] == m - 1:
            hero_coords[1] = 0
        else:
            hero_coords[1] += 1

    # чи не спіймав курку
    catched_animals = []
    for animal in animals:
        if animal[4] == hero_coords:
            catched_animals.append(animal)
            hero_details += animal[5]

    # видаляємо пійманих курок зі списку
    for animal in catched_animals:
        animals.remove(animal)

    # хід тварин
    for animal in animals:
        if animal[0] == 'kurka':
            direction = random.choice(['w', 'a', 's', 'd'])
            if direction == 'w':
                if animal[4][0] != 0:
                    animal[4][0] -= 1
            elif direction == 'a':
                if animal[4][1] == 0:
                    animal[4][1] = m - 1
                else:
                    animal[4][1] -= 1
            elif direction == 's':
                if animal[4][0] != n - 1:
                    animal[4][0] += 1
            elif direction == 'd':
                if animal[4][1] == m - 1:
                    animal[4][1] = 0
                else:
                    animal[4][1] += 1
            
        elif animal[0] == 'олень':
            pass

    # чи не спіймав курку
    catched_animals = []
    for animal in animals:
        if animal[4] == hero_coords:
            catched_animals.append(animal)
            hero_details += animal[5]

    # видаляємо пійманих курок зі списку
    for animal in catched_animals:
        animals.remove(animal)

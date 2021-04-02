import random


class Human:
    name = 'Bob'
    age = 0
    is_male = True


def count_girls_and_boys(humans):
    b_count = 0
    g_count = 0
    for human in humans:
        if human.is_male:
            b_count += 1
        else:
            g_count += 1
    return b_count, g_count


def create_random_person():
    h = Human()
    h.age = random.randint(1, 120)
    h.is_male = random.choice([True, False])
    h.name = random.choice(['Bob', 'Katia', 'Leha', 'Klara', 'Ilya'])
    return h


h1 = Human()
h1.name = 'Marina'
h1.age = 20
h1.is_male = False

h2 = Human()
h2.name = 'Vasya'
h2.age = 25

h3 = Human()
h3.age = 14


people = [h1, h2, h3]

people2 = [create_random_person() for _ in range(100)]

for human in people2:
    print(human.name, human.age, human.is_male)

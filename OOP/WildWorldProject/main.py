import random
from os import system


N = 20
M = 30


def clear():
    system('cls')


class GameObject:
    sprite = ''

    def __init__(self, i, j, is_solid=False):
        self.i = i
        self.j = j
        self.is_solid = is_solid

    def draw(self, matrix):
        matrix[self.i][self.j] = self.sprite


class Creature(GameObject):
    def __init__(self, name, i, j, is_alive, hp, satiety, water, creatures, armor=0):
        super().__init__(i, j)
        self.name = name
        self.is_alive = is_alive
        self.hp = self.max_hp = hp
        self.satiety = self.max_satiety = satiety
        self.water = self.max_water = water
        self.creatures = creatures
        self.armor = armor

    def get_damage(self, damage):
        rem_damage = damage - self.armor
        if rem_damage > 0:
            self.loose_hp(rem_damage)

    def loose_hp(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.die()

    def die(self):
        self.is_alive = False

    def heal(self, hp):
        self.hp += hp
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def move(self, direction, speed=1):
        if direction == 'w':
            if self.i != 0:
                self.i -= 1
        elif direction == 'a':
            if self.j == 0:
                self.j = M - 1
            else:
                self.j -= 1
        elif direction == 's':
            if self.i != N - 1:
                self.i += 1
        elif direction == 'd':
            if self.j == M - 1:
                self.j = 0
            else:
                self.j += 1

    def make_move(self):
        raise NotImplementedError

    def __str__(self):
        return f"Creature {self.sprite} {self.name} ([{self.i}, {self.j}])"

    def __repr__(self):
        return self.__str__()


class Chicken(Creature):
    sprite = 'c'

    def __init__(self, name, i, j, hp, satiety, water, creatures, armor=0):
        super().__init__(name, i, j, True, hp, satiety, water, creatures, armor)

    def make_move(self):
        direction = random.choice(['w', 'a', 's', 'd'])
        self.move(direction)


def create_matrix():
    return [['-' for _ in range(M)] for _ in range(N)]


def print_matrix(matrix):
    text = ''
    for row in matrix:
        text += '|'
        for el in row:
            text += str(el) + ' '
        text = text[:-1] + '|\n'
    print(text)


creatures = []
creatures.append(Chicken('Chika', i=3, j=2, hp=5, satiety=5, water=5, creatures=creatures))
creatures.append(Chicken('Biba', i=6, j=2, hp=5, satiety=5, water=5, creatures=creatures))
creatures.append(Chicken('Ryaba', i=5, j=5, hp=5, satiety=5, water=5, creatures=creatures))


while True:
    clear()
    matrix = create_matrix()
    for obj in creatures:
        obj.draw(matrix)
    print_matrix(matrix)

    for creature in creatures:
        creature.make_move()
    input()

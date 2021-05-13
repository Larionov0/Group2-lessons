import random
from os import system
import colorama

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
    def __init__(self, i, j, hp, world, armor=0, is_alive=True):
        super().__init__(i, j)
        self.is_alive = is_alive
        self.hp = self.max_hp = hp
        self.world = world
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
        return f"Creature {self.sprite} ([{self.i}, {self.j}])"

    def __repr__(self):
        return self.__str__()


class Animal(Creature):
    def __init__(self, name, i, j, hp, satiety, water, world, armor=0, is_alive=True):
        super().__init__(i, j, hp, world, armor, is_alive)
        self.name = name
        self.satiety = self.max_satiety = satiety
        self.water = self.max_water = water

    def loose_satiety(self, satiety):
        self.satiety -= satiety
        if self.satiety <= 0:
            self.die()

    def get_satiety_color(self):
        part = self.satiety / self.max_satiety * 100  # відсотки

        if part >= 70:
            return colorama.Fore.GREEN
        elif part >= 40:
            return colorama.Fore.YELLOW
        else:
            return colorama.Fore.RED

    def draw(self, matrix):
        matrix[self.i][self.j] = self.get_satiety_color() + self.sprite + colorama.Fore.RESET

    def __str__(self):
        return f"Creature {self.sprite} {self.name} ([{self.i}, {self.j}])"


class Plant(Creature):
    pass


class Grassy(Plant):
    sprite = '*'

    def __init__(self, i, j, satiety, hp, world, armor=0, is_alive=True):
        super().__init__(i, j, hp, world, armor, is_alive)
        self.satiety = satiety

    def make_move(self):
        pass

    @classmethod
    def spawn(cls, world):
        new_grassy = cls(
            i=random.randint(0, N - 1),
            j=random.randint(0, M - 1),
            satiety=random.choice([1, 1, 1, 2, 2, 3]),
            hp=1,
            world=world
        )
        world.creatures.append(new_grassy)

    @classmethod
    def check_spawn(cls, world, round_):
        if round_ % 1 == 0:
            cls.spawn(world)
            cls.spawn(world)


class Chicken(Animal):
    names = ['Ryaba', 'Isabella', 'Maria', 'Katia', 'Klava']
    sprite = 'c'

    def __init__(self, name, i, j, hp, satiety, water, world, armor=0):
        super().__init__(name, i, j, hp, satiety, water, world, armor)

    def get_grassies(self):
        result_list = []
        for creature in self.world.get_alive_creatures():
            if isinstance(creature, Grassy):
                if creature.i == self.i and creature.j == self.j:
                    result_list.append(creature)
        return result_list

    def make_move(self):
        direction = random.choice(['w', 'a', 's', 'd'])
        self.move(direction)

        grassies = self.get_grassies()
        if grassies:
            grassies[0].die()
            self.satiety = self.max_satiety
            Chicken.spawn_in_position(self.world, self.i, self.j)
            Chicken.spawn_in_position(self.world, self.i, self.j)
            Chicken.spawn_in_position(self.world, self.i, self.j)

        self.loose_satiety(1)

    @classmethod
    def spawn_in_position(cls, world, i, j):
        new_chicken = cls(
            name=random.choice(cls.names),
            i=i,
            j=j,
            hp=3,
            satiety=random.choices([8, 9, 10], [1, 3, 1])[0],
            water=0,  #
            world=world
        )
        world.creatures.append(new_chicken)

    @classmethod
    def spawn(cls, world):
        i = random.randint(0, N - 1)
        j = random.randint(0, M - 1)
        cls.spawn_in_position(world, i, j)


class SmartChicken(Chicken):
    sprite = 'S'

    def __init__(self, name, i, j, hp, satiety, water, world, armor=0):
        super().__init__(name, i, j, hp, satiety, water, world, armor)

    def make_move(self):
        for el in self.world.creatures:
            if isinstance(el, Grassy):
                vectorX = el.i - self.i
                vectorY = el.j - self.j
                if vectorX == 0 and vectorY > 0:
                    direction = 's'
                elif vectorX == 0 and vectorY < 0:
                    direction = 'w'
                elif vectorX > 0 and vectorY == 0:
                    direction = 'd'
                elif vectorX < 0 and vectorY == 0:
                    direction = 'a'
                else:
                    direction = random.choice(['w', 'a', 's', 'd'])
                break

        self.move(direction)

        grassies = self.get_grassies()
        if grassies:
            grassies[0].die()
            self.satiety = self.max_satiety
            SmartChicken.spawn_in_position(self.world, self.i, self.j)
            SmartChicken.spawn_in_position(self.world, self.i, self.j)
            Chicken.spawn_in_position(self.world, self.i, self.j)

        self.loose_satiety(1)


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


class World:
    def __init__(self):
        self.creatures = []
        self.objects = []
        for _ in range(3):
            SmartChicken.spawn(self)
        for _ in range(15):
            Grassy.spawn(self)

    def get_alive_creatures(self):
        return list(filter(lambda creature: creature.is_alive is True, self.creatures))

    def run(self):
        years = 1

        round_ = 1
        while True:
            if round_ % years == 0:
                clear()
                matrix = create_matrix()
                for obj in self.get_alive_creatures():
                    obj.draw(matrix)
                print_matrix(matrix)

            # lst = [creature.satiety for creature in self.creatures if isinstance(creature, Animal)]
            # print(lst)

            for creature in self.get_alive_creatures():
                creature.make_move()

            Grassy.check_spawn(self, round_)

            if round_ % years == 0:
                input()

            round_ += 1


w = World()
w.run()


import random
from os import system
import colorama

colorama.init()

N = 30
M = 40


def clear():
    system('cls')


def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


class GameObject:
    sprite = ''

    def __init__(self, i, j, is_solid=False):
        self.i = i
        self.j = j
        self.is_solid = is_solid

    def distance(self, other):
        return distance([self.i, self.j], [other.i, other.j])

    def draw(self, matrix):
        matrix[self.i][self.j] = self.sprite


class Creature(GameObject):
    def __init__(self, i, j, hp, world, armor=0, is_alive=True):
        super().__init__(i, j)
        self.is_alive = is_alive
        self.hp = self.max_hp = hp
        self.world = world
        self.armor = armor

    def get_all_creatures_in_radius(self, radius):
        creatures_in_radius = []
        for creature in self.world.get_alive_creatures():
            if self.distance(creature) <= radius and self is not creature:
                creatures_in_radius.append(creature)
        return creatures_in_radius

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

    def get_grassies(self):
        result_list = []
        for creature in self.world.get_alive_creatures():
            if isinstance(creature, Grassy):
                if creature.i == self.i and creature.j == self.j:
                    result_list.append(creature)
        return result_list

    def move_to_point(self, target_point):
        points = {
            'w': [self.i - 1, self.j],
            's': [self.i + 1, self.j],
            'a': [self.i, self.j - 1],
            'd': [self.i, self.j + 1]
        }

        cur_min = float('inf')
        min_dir = None
        for direction, point in points.items():
            d = distance(point, target_point)
            if d < cur_min:
                cur_min = d
                min_dir = direction

        self.move(min_dir)

    def restore_satiety(self, satiety):
        self.satiety += satiety
        if self.satiety > self.max_satiety:
            self.satiety = self.max_satiety

    def loose_satiety(self, satiety):
        self.satiety -= satiety
        if self.satiety <= 0:
            self.die()

    def get_satiety_color(self):
        part = self.satiety / self.max_satiety * 100  # відсотки

        if part >= 70:
            return colorama.Fore.BLUE
        elif part >= 40:
            return colorama.Fore.YELLOW
        else:
            return colorama.Fore.RED

    def draw(self, matrix):
        matrix[self.i][self.j] = self.get_satiety_color() + self.sprite + colorama.Fore.RESET

    @classmethod
    def spawn_in_position(cls, world):
        raise NotImplementedError

    @classmethod
    def spawn(cls, world):
        i = random.randint(0, N - 1)
        j = random.randint(0, M - 1)
        cls.spawn_in_position(world, i, j)

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
            for _ in range(3):
                cls.spawn(world)


class Chicken(Animal):
    names = ['Ryaba', 'Isabella', 'Maria', 'Katia', 'Klava']
    sprite = 'c'

    def __init__(self, name, i, j, hp, satiety, water, world, armor=0):
        super().__init__(name, i, j, hp, satiety, water, world, armor)

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


class BlueRabbit(Animal):
    sprite = 'r'
    radius = 3
    names = ['Pupsen', 'Vupsen']

    def make_move(self):
        cur_min = float('inf')
        nearest_grassy = None
        for creature in self.get_all_creatures_in_radius(self.radius):
            if isinstance(creature, Grassy):
                d = self.distance(creature)
                if d < cur_min:
                    cur_min = d
                    nearest_grassy = creature

        if nearest_grassy:
            self.move_to_point([nearest_grassy.i, nearest_grassy.j])
        else:
            self.move(random.choice(['w', 'a', 's', 'd']))

        grassies = self.get_grassies()
        if grassies:
            grassies[0].die()
            self.restore_satiety(grassies[0].satiety * 3 + 2)

        self.loose_satiety(1)

    @classmethod
    def spawn_in_position(cls, world, i, j):
        new_rabbit = cls(
            name=random.choice(cls.names),
            i=i,
            j=j,
            hp=5,
            satiety=random.randint(5, 9) + random.randint(5, 9) + random.randint(5, 9),
            water=0,  #
            world=world
        )
        world.creatures.append(new_rabbit)


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
        # for _ in range(10):
        #     Chicken.spawn(self)
        for _ in range(20):
            BlueRabbit.spawn(self)
        for _ in range(60):
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

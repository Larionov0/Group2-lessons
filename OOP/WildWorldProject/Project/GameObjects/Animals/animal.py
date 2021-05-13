import random
from ..creature import Creature
import colorama
from ...settings import N, M
from ...functions import *
from ..Plants.grassy import Grassy


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

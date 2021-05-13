from ..functions import distance
from ..settings import N, M


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

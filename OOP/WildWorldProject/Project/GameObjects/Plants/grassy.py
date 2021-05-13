import random
from .plant import Plant
from ...settings import N, M


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

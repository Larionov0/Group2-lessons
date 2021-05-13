import random
from .animal import Animal


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
